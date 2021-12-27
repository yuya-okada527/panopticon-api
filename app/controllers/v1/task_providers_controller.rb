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
end
