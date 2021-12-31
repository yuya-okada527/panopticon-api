class TaskStatusHistory < ApplicationRecord
  # Relation
  belongs_to :task, dependent: :destroy

  # Enum
  enum status: { created: 0, todo: 1, doing: 2, done: 3, closed: 4 }, _prefix: true
end
