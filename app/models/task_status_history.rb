class TaskStatusHistory < ApplicationRecord
  # Relation
  has_many :tasks, dependent: :destroy
end
