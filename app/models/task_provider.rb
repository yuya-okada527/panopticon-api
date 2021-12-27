class TaskProvider < ApplicationRecord
  # Relation
  has_many :tasks, dependent: :destroy

  # Enum
  enum provider_kind: { user: 0, github: 1 }, _prefix: true
end
