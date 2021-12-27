Rails.application.routes.draw do
  get '/v1/projects', to: 'v1/projects#projects_get'
  get '/v1/projects/:project_id/tasks', to: 'v1/tasks#tasks_get'
  get '/v1/projects/:project_id/tasks/:task_id', to: 'v1/tasks#tasks_task_id_get'
end
