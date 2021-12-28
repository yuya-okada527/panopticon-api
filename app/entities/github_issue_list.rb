class GithubIssueList

  def initialize(json = [])
    @github_issues = json.map do |issue|
      GithubIssue.new(issue)
    end
  end

  def extend!(json)
    json.each do |issue|
      @github_issues << GithubIssue.new(issue)
    end
  end
end
