class Task < ApplicationRecord

  # Relation
  belongs_to :project
  belongs_to :task_provider, optional: true
  has_many :task_status_histories, dependent: :destroy

  # Enum
  enum status: { created: 0, todo: 1, doing: 2, done: 3, closed: 4 }, _prefix: true

  # Scope
  scope :by_task_id, -> (task_id) { where(id: task_id) if task_id.present? }
  scope :by_project_id, -> (project_id) { where(project_id: project_id) if project_id.present? }
  scope :by_status, -> (status_list) { where(status: status_list) if status_list.present? }

  # instance method
  def external_url
    return if self.task_provider.nil? || self.task_provider.provider_kind_user?
    self.task_provider.provider_url
  end
end
