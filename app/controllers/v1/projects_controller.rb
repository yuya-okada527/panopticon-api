class V1::ProjectsController < ApplicationController
  def index
    @projects = Project.all
    render :template => 'projects_index.json.jb'
  end
end
