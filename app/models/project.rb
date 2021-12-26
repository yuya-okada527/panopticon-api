class Project < ApplicationRecord

  # Relation
  has_many :tasks, dependent: :destroy
  has_many :task_providers, dependent: :destroy
end
