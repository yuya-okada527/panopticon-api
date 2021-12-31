# TODO: データの交換方法は変える
# データ初期化(暫定対応)
Project.destroy_all
TaskProvider.destroy_all
Task.destroy_all
TaskStatusHistory.destroy_all
ActiveRecord::Base.connection.execute('ALTER TABLE projects AUTO_INCREMENT = 1')
ActiveRecord::Base.connection.execute('ALTER TABLE task_providers AUTO_INCREMENT = 1')
ActiveRecord::Base.connection.execute('ALTER TABLE tasks AUTO_INCREMENT = 1')
ActiveRecord::Base.connection.execute('ALTER TABLE task_status_histories AUTO_INCREMENT = 1')

# プロジェクト
project = Project.new(name: "Local Project")
project.save!

# タスクプロバイダ
api_task_provider = TaskProvider.new(
  project_id: project.id,
  name: "Panopticon API",
  provider_kind: 1,
  organization: "yuya-okada527",
  repository: "panopticon-api"
)
api_task_provider.save!

fe_task_provider = TaskProvider.new(
  project_id: project.id,
  name: "Panopticon FE",
  provider_kind: 1,
  organization: "yuya-okada527",
  repository: "panopticon-fe"
)
fe_task_provider.save!

# タスク
[
  {
    project_id: project.id,
    task_provider_id: api_task_provider.id,
    name: "task1",
    description: "# Task1\n\n- list1\n- list2",
    status: 1
  }
].each do |args|
  task = Task.new(**args)
  task.save!
  # タスクステータス履歴
  [
    {
      task_id: task.id,
      before_status: 0,
      after_status: 1
    }
  ].each do |args|
    history = TaskStatusHistory.new(**args)
    history.save!
  end
end
