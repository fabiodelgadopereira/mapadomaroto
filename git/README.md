Create branch
```bash
git branch dev
```

Switch branch
```bash
git checkout dev
```

push to specific branch
```bash
git push --set-upstream origin dev
```

remove
```bash
git rm file
```


git config list
```bash
git config -l
```

Erro: Message "Support for password authentication was removed."

Use My Account → Settings → Developer settings → Personal access tokens → Generate new token.
```bash
git remote set-url origin https://<token>@github.com/<username>/<repo>
```
https://stackoverflow.com/questions/68775869/message-support-for-password-authentication-was-removed