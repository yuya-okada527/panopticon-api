class V1::ProjectsController < ApplicationController
  def projects_get
    @projects = Project.all
    render :template => 'projects_get.json.jb'
  end
end
