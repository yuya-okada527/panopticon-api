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
    # TODO: project_idで絞るのは、共通にしても良いかも
    task = Task
      .by_project_id(params[:project_id])
      .by_task_id(params[:task_id])
      .first

    # 遷移前後の状態を取得しておく
    before_status = task.status
    after_status = params[:status] if params[:status].present?
    task.name = params[:name] if params[:name].present?
    task.description = params[:description] if params[:description].present?
    task.status = after_status if after_status.present?
    status_history = TaskStatusHistory.new(
      task_id: task.id,
      before_status: TaskStatusHistory.statuses[before_status],
      after_status: TaskStatusHistory.statuses[after_status]
    )
    ActiveRecord::Base.transaction do
      task.task_status_histories << status_history if task.will_save_change_to_status?
      task.save!
    end
    render :template => 'tasks_task_id_put.json.jb', :locals => { :id => task.id }
  end

  def tasks_task_id_status_put
    before_status = params.require(:before_status)
    after_status = params.require(:after_status)
    task = Task
      .by_project_id(params[:project_id])
      .by_task_id(params[:task_id])
      .by_status(before_status)
      .first
    # TODO この辺のハンドリング方法は、検討
    render json: {status: 404}, status: 404 if !task.present?
    task.status = after_status
    status_history = TaskStatusHistory.new(
      task_id: task.id,
      before_status: TaskStatusHistory.statuses[before_status],
      after_status: TaskStatusHistory.statuses[after_status]
    )
    ActiveRecord::Base.transaction do
      task.task_status_histories << status_history
      task.save!
    end
    render :template => 'tasks_task_id_status_put', :locals => { :id => task.id }
  end

end
