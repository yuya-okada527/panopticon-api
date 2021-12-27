class TaskProvider < ApplicationRecord
  # Relation
  has_many :tasks, dependent: :destroy

  # Enum
  enum provider_kind: { user: 0, github: 1 }, _prefix: true

  # Scope
  scope :by_project_id, -> (project_id) { where(project_id: project_id) if project_id.present? }
end
