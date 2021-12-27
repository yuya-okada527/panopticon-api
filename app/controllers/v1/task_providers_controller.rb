class V1::TaskProvidersController < ApplicationController

  def task_providers_get
    @task_providers = TaskProvider.by_project_id(params[:project_id])
    render :template => 'task_providers_get.json.jb'
  end
end
