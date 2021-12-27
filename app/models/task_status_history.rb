class TaskStatusHistory < ApplicationRecord
  # Relation
  belongs_to :task, dependent: :destroy
end
