# TODO: データの交換方法は変える
Project.destroy_all
ActiveRecord::Base.connection.execute('ALTER TABLE projects AUTO_INCREMENT = 1')
project = Project.new(name: "Local Project")
project.save!
