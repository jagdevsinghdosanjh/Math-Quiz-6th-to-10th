# Get current folder name as repo name
$projectPath = Get-Location
$projectName = Split-Path $projectPath -Leaf
$githubUsername = "jagdevsinghdosanjh"
$remoteUrl = "https://github.com/$githubUsername/$projectName.git"

# Check if GitHub CLI is installed
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Error "❌ GitHub CLI (gh) is not installed. Install it from https://cli.github.com/"
    exit
}

# Step 1: Remove old Git history
Write-Host "🧹 Removing old Git history..."
Remove-Item -Recurse -Force .git -ErrorAction SilentlyContinue

# Step 2: Initialize new Git repo
Write-Host "🔧 Initializing new Git repository..."
git init

# Step 3: Add and commit files
Write-Host "📦 Adding and committing files..."
git add .
git commit -m "Initial commit"

# Step 4: Create GitHub repo if it doesn't exist
Write-Host "🌐 Checking if GitHub repo exists..."
$repoCheck = gh repo view "$githubUsername/$projectName" --json name -q .name 2>$null

if (-not $repoCheck) {
    Write-Host "📁 Creating GitHub repository '$projectName'..."
    gh repo create "$githubUsername/$projectName" --public --source . --remote origin --push
} else {
    Write-Host "🔗 Repo already exists. Setting remote origin..."
    git remote add origin $remoteUrl
    git branch -M main
    git push -u origin main
}

Write-Host "✅ Project '$projectName' successfully uploaded to GitHub!"

# Run the script in terminal using command
# .\initialize-git.ps1
