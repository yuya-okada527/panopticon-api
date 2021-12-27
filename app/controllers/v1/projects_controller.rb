class V1::ProjectsController < ApplicationController
  def projects_get
    @projects = Project.all
    render :template => 'projects_index.json.jb'
  end
end
