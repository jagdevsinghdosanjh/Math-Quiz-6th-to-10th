# Get current folder name as repo name
$projectPath = Get-Location
$projectName = Split-Path $projectPath -Leaf
$githubUsername = "jagdevsinghdosanjh"
$remoteUrl = "https://github.com/$githubUsername/$projectName.git"

# Step 1: Prompt user to create GitHub repo manually
Write-Host "⚠️ Please make sure the GitHub repository '$projectName' exists at:"
Write-Host "$remoteUrl"
Write-Host ""
Write-Host "👉 Open this link to create it: https://github.com/new"
Write-Host "   - Repository name: $projectName"
Write-Host "   - Leave it empty (no README, .gitignore, or license)"
Write-Host ""
Read-Host "Press Enter once the repository is created"

# Step 2: Remove old Git history
Write-Host "🧹 Removing old Git history..."
Remove-Item -Recurse -Force .git -ErrorAction SilentlyContinue

# Step 3: Initialize new Git repo
Write-Host "🔧 Initializing new Git repository..."
git init

# Step 4: Add and commit files
Write-Host "📦 Adding and committing files..."
git add .
git commit -m "Initial commit"

# Step 5: Set remote origin and push
Write-Host "🔗 Setting remote origin to $remoteUrl"
git remote add origin $remoteUrl
git branch -M main
Write-Host "🚀 Pushing to GitHub..."
git push -u origin main

Write-Host "✅ Project '$projectName' successfully pushed to GitHub!"

# Run the script in terminal using command
# .\initialize-git.ps1
