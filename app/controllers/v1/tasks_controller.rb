class V1::TasksController < ApplicationController

  def tasks_get
    @tasks = Task
      .by_project_id(params[:project_id])
      .by_status(params[:status])
      .by_keyword(params[:keyword])
    render :template => 'tasks_get.json.jb'
  end

  def tasks_post
    name = params.require(:name)
    description = params.require(:description)
    project_id = params.require(:project_id)
    task = Task.new(name: name, description: description, project_id: project_id)
    task.save!
    render :template => 'tasks_post.json.jb', :locals => { :id => task.id }
  end

  def tasks_task_id_get
    @task = Task
      .by_task_id(params[:task_id])
      .by_project_id(params[:project_id])
      .first
    render :template => 'tasks_task_id_get.json.jb'
  end

  def tasks_task_id_put
    task = Task
      .by_project_id(params[:project_id])
      .by_task_id(params[:task_id])
      .first
    task.name = params[:name] if params[:name].present?
    task.description = params[:description] if params[:description].present?
    task.save!
    render :template => 'tasks_task_id_put.json.jb', :locals => { :id => task.id }
  end

end
