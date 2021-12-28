class V1::TaskProvidersController < ApplicationController

  def task_providers_get
    @task_providers = TaskProvider.by_project_id(params[:project_id])
    render :template => 'task_providers_get.json.jb'
  end

  def task_providers_post
    task_provider = TaskProvider.new(
      project_id: params[:project_id],
      name: params.require(:name),
      provider_kind: params.require(:provider_kind),
      provider_url: params[:provider_url] || ""
    )
    task_provider.save!
    render :template => 'task_providers_post.json.jb', :locals => { :id => task_provider.id }
  end

  def task_providers_task_provider_id_delete
    task_provider = TaskProvider
      .by_project_id(params[:project_id])
      .find(params[:task_provider_id])
    render json: { status: 404 }, status: 404 if !task_provider.present?
    task_provider.destroy!
    render :template => 'task_providers_task_provider_id_delete.json.jb', :locals => { :id => task_provider.id }
  end

  def task_providers_task_provider_id_sync_post
    project_id = params[:project_id]
    task_provider = TaskProvider
      .by_project_id(project_id)
      .find(params[:task_provider_id])
    render json: { status: 404 }, status: 404 if !task_provider.present?
    token = request.headers["X-Task-Provider-Token"]
    user_name = params[:user_name]
    github_issue_list = GithubRepository.fetch_all_issues(
      task_provider.organization,
      task_provider.repository,
      token
    )
    github_issue_list.filter_by_assignees!(user_name)
    ActiveRecord::Base.transaction do
      github_issue_list.tasks.each do |task|
        task.project_id = project_id
        task.task_provider = task_provider
        task.save!
      end
    end
  end
end
