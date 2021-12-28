class GithubIssueList

  def initialize(json)
    @github_issues = json.map do |issue|
      GithubIssue.new(issue)
    end
  end
end
