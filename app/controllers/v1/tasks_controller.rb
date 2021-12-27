class V1::TasksController < ApplicationController

  def tasks_get
    project_id = params[:project_id]
    status = params[:status]
    @tasks = Task
      .by_project_id(project_id)
      .by_status(status)
    render :template => 'tasks_get.json.jb'
  end

end
