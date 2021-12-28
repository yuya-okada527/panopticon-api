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

  def filter_by_assignees!(assignee)
    @github_issues = @github_issues.filter do |issue|
      issue.assignees.includes(assignee)
    end
  end

  def tasks
    @github_issues.map do |issue|
      task = Task.find_or_initialize_by(
        external_id: issue.number,
        external_url: issue.html_url
      )
      task.name = issue.title
      task.description = issue.body
    end
  end
end
