# TODO: データの交換方法は変える
# プロジェクト
Project.destroy_all
ActiveRecord::Base.connection.execute('ALTER TABLE projects AUTO_INCREMENT = 1')
project = Project.new(name: "Local Project")
project.save!

# タスク
Task.destroy_all
ActiveRecord::Base.connection.execute('ALTER TABLE tasks AUTO_INCREMENT = 1')
[
  {
    project_id: project.id,
    name: "task1",
    description: "# Task1\n\n- list1\n- list2",
    status: 0
  }
].each do |args|
  task = Task.new(**args)
  task.save!
end
