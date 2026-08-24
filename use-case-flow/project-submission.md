# Use-Case Flow Specification

## Use Case: Submit Project

### Preconditions

1. The Student Team is registered in the system.
2. The Student Team is logged into the application.
3. The project profile has been created.
4. Required project information and artifacts are available.

### Postconditions

1. The project submission is stored successfully.
2. The submitted project is available in the showcase system for review.
3. The GitHub repository URL has been validated.
4. The Student Team receives confirmation of successful submission.

### Main Success Scenario

1. The Student Team logs into the Student Project Portfolio & Showcase App.
2. The Student Team opens the project submission section.
3. The system displays the required project information fields.
4. The Student Team enters the project title and abstract.
5. The Student Team provides the demo video link.
6. The Student Team enters the GitHub repository URL.
7. The system validates the GitHub repository URL.
8. The Student Team uploads the required multimedia artifacts.
9. The Student Team submits the project.
10. The system validates all required information.
11. The system stores the project submission.
12. The system displays a submission confirmation to the Student Team.

### Alternate Flow

**A1. Invalid GitHub Repository URL**

1. The Student Team enters an invalid GitHub repository URL.
2. The system validates the URL and detects that it is invalid.
3. The system displays an error message.
4. The Student Team corrects the GitHub repository URL.
5. The system validates the corrected URL.
6. The submission process continues from Step 8 of the Main Success Scenario.