import subprocess

def get_contributors():
    # Run the git log command to get the authors of commits
    try:
        # 'git log --format=%aN' returns only the names of the authors
        result = subprocess.run(['git', 'log', '--format=%aN'], stdout=subprocess.PIPE, text=True)
        contributors = result.stdout.strip().split('\n')
        
        # Get unique contributors by converting the list to a set
        unique_contributors = set(contributors)
        
        # Print contributors
        print("Contributors:")
        for contributor in unique_contributors:
            print(contributor)

    except Exception as e:
        print(f"Error: {e}")

# Call the function
get_contributors()
#another one
