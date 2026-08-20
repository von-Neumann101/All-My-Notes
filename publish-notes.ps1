$ErrorActionPreference = 'Stop'

$repoRoot = $PSScriptRoot
$sourceRoot = 'D:\Desktop\All-notes'
$contentRoot = Join-Path $repoRoot 'content'
$indexPath = Join-Path $contentRoot 'index.md'

if (-not (Test-Path -LiteralPath $sourceRoot -PathType Container)) {
  throw ('Notes folder not found: {0}' -f $sourceRoot)
}

$branch = git -C $repoRoot branch --show-current
if ($LASTEXITCODE -ne 0 -or $branch.Trim() -ne 'v5') {
  throw ('Publish from the v5 branch. Current branch: {0}' -f $branch)
}

git -C $repoRoot diff --cached --quiet
if ($LASTEXITCODE -eq 1) {
  throw 'The Git index already has staged changes. Commit or unstage them first.'
}
if ($LASTEXITCODE -ne 0) {
  throw 'Could not inspect staged changes.'
}

if (-not (Test-Path -LiteralPath $indexPath -PathType Leaf)) {
  throw ('Repository-owned page not found: {0}' -f $indexPath)
}

$indexBytes = [System.IO.File]::ReadAllBytes($indexPath)
try {
  & robocopy $sourceRoot $contentRoot /MIR /XJ /R:2 /W:1 /XD .git .obsidian /XF .git .gitignore .gitattributes .gitmodules '*.pdf' /NJH /NJS /NP
  if ($LASTEXITCODE -ge 8) {
    throw ('Notes sync failed. Robocopy exit code: {0}' -f $LASTEXITCODE)
  }
}
finally {
  [System.IO.File]::WriteAllBytes($indexPath, $indexBytes)
}

git -C $repoRoot add -- content
if ($LASTEXITCODE -ne 0) {
  throw 'Could not stage content.'
}

git -C $repoRoot diff --cached --quiet -- content
if ($LASTEXITCODE -eq 0) {
  Write-Host 'No note changes to publish.'
  exit 0
}
if ($LASTEXITCODE -ne 1) {
  throw 'Could not inspect note changes.'
}

$commitMessage = 'publish notes: {0}' -f (Get-Date -Format 'yyyy-MM-dd HH:mm')
git -C $repoRoot commit -m $commitMessage
if ($LASTEXITCODE -ne 0) {
  throw 'Could not commit notes.'
}

git -C $repoRoot push origin v5
if ($LASTEXITCODE -ne 0) {
  throw 'Could not push notes.'
}

Write-Host 'Published. GitHub Pages will update shortly.'
Write-Host 'https://von-neumann101.github.io/All-My-Notes/'
