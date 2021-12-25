class SamplesController < ApplicationController
  def index
    @sample = {id: '001', name: 'sample'}
    render :template => 'samples_index.json.jb'
  end
end
