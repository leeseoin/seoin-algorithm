---
name: emulator
description: CCTV 에뮬레이터 40채널 시작/종료. 사용법 /emulator start|stop|status
---

# CCTV 에뮬레이터 제어

$ARGUMENTS 명령을 실행한다.

## 명령어

### start
1. mediamtx가 실행 중인지 확인 (`lsof -i :8553`)
2. 실행 중이 아니면 사용자에게 알림: "mediamtx를 먼저 실행하세요: `mediamtx mediamtx.yml`"
3. `./start-emulators.sh` 실행 (백그라운드)
4. 5초 대기 후 go2rtc 스트림 목록 확인: `curl -s http://localhost:1984/api/streams | python3 -m json.tool | head -20`
5. 결과 출력

### stop
1. `./stop-emulators.sh` 실행
2. 남은 FFmpeg 프로세스 확인: `pgrep -f "ffmpeg.*emu"`
3. 결과 출력

### status
1. mediamtx 상태: `lsof -i :8553`
2. FFmpeg 에뮬레이터 프로세스 수: `pgrep -fc "ffmpeg.*emu"`
3. go2rtc 등록 스트림 수: `curl -s http://localhost:1984/api/streams | python3 -c "import sys,json; print(len(json.load(sys.stdin)))"`
4. go2rtc 메모리: `curl -s http://localhost:8085/api/monitor | python3 -m json.tool`

## 주의사항
- 프로젝트 루트 디렉토리: /Users/iseoin/SpringBoot_project/webrtc
- start-emulators.sh는 mediamtx가 :8553에서 실행 중이어야 동작
- Spring Boot(go2rtc)도 실행 중이어야 스트림 확인 가능
