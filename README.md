Python Quiz Game
Python 콘솔 기반 퀴즈 게임입니다.

Codyssey Pre-course 과제 수행을 위해 제작되었습니다

Troubleshooting
Git Remote 중복 오류
문제

git remote add origin 실행 시

error: remote origin already exists

발생

원인

이미 origin 원격 저장소가 등록되어 있었다.

해결

git remote remove origin

git remote add origin [repository-url]

명령어로 기존 원격 저장소를 제거 후 다시 등록하였다.