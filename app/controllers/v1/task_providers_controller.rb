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
end
