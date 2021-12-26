class Task < ApplicationRecord
  # Relation
  belongs_to :project
  belongs_to :task_provider
  has_many :task_status_histories, dependent: :destroy
end
