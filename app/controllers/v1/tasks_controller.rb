class V1::TasksController < ApplicationController

  def tasks_get
    project_id = params[:project_id]
    status = params[:status]
    keyword = params[:keyword]
    @tasks = Task
      .by_project_id(project_id)
      .by_status(status)
      .by_keyword(keyword)
    render :template => 'tasks_get.json.jb'
  end

  def tasks_task_id_get
    @task = Task
      .by_task_id(params[:task_id])
      .by_project_id(params[:project_id])
      .first
    render :template => 'tasks_task_id_get.json.jb'
  end

end
