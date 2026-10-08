# My AI Engineering Path

<!-- Managed by the ai-engineering-from-scratch learning skills.
     Repo: https://github.com/rohitg00/ai-engineering-from-scratch -->

## Mission

AI와 머신러닝의 수학적·프로그래밍적 원리를 이해하기. Python으로 알고리즘을 직접 구현하기. LLM, RAG, MCP, AI Agent의 구조와 작동 원리를 이해하기. 최종적으로 AI 기반 서비스를 직접 설계하고 개발할 수 있는 능력 갖추기.

한국어로 설명하되 주요 영어 기술 용어를 병기한다.

최종 제작물: 아직 미정. 기초를 익힌 뒤 결정한다. Python을 주력 언어로 사용한다.

## Placement

- Date: 2026-10-08 (Asia/Seoul)
- Score: 4/10 — Math & Statistics: 1/2; Classical ML: 2/2; Deep Learning: 0/2; NLP & Transformers: 0/2; Applied AI: 1/2.
- Entry point: Phase 0: Setup & Tooling (실제 학습 계획). 공식 점수 매핑의 추천은 Phase 3: Deep Learning Core이며, 아래에 차이를 기록한다.
- Pace: 가능한 한 빠르게. 주당 시간은 미지정이며 임의로 정하지 않는다.

자기 보고: Python 기초 문법은 알지만 심화 프로그래밍 경험이 부족하다. Pandas, Git, API, Docker 이해가 부족하며 AI가 작성한 코드를 주로 사용해 작동 원리를 충분히 이해하지 못한다. 이는 자기 보고이며 실기 능력이나 수학 수준이 검증된 것은 아니다.

현재 학습 상태: 온보딩·공식 배치 평가 완료. 2026-10-08 Phase 0의 첫 수업 Dev Environment 완료, 공식 post 퀴즈 3/3점. Python/NumPy 점검과 내적, 가상환경 활성화·해제, Python/JavaScript/Rust Hello World, CPU PyTorch 텐서 계산을 직접 작성·실행했다. Julia 설치는 공식 선택 항목으로 보류했고, CUDA/MPS 백엔드를 사용할 수 없어 실제 GPU 계산은 미수행이다. 네 언어 전체 실습 완료로 표기하지 않는다.

다음 세션: 이 파일과 skills/learn/SKILL.md를 읽고 Phase 0 · 02 Git & Collaboration을 진행한다. 첫 수업 퀴즈에서 짧게 복습한 뒤 설명 → 직접 구현 → 실행·검증 → 평가 순서를 따른다. 사용자는 새 용어를 먼저 정의하고 필요성 → 개념 → 명령 → 실제 효과를 연결하는 친절한 설명을 요구했다. 설명하지 않은 내용을 먼저 퀴즈로 묻지 않는다.

배치 응답 기록:

| Question | Learner answer | Result |
|----------|----------------|--------|
| Q1 | 모르겠음 | 0 |
| Q2 | D | 1 |
| Q3 | B | 1 |
| Q4 | C | 1 |
| Q5 | 모르겠음 | 0 |
| Q6 | 모르겠음 | 0 |
| Q7 | 모르겠음 | 0 |
| Q8 | 모르겠음 | 0 |
| Q9 | 모르겠음 | 0 |
| Q10 | B | 1 |

해석: 내적(dot product), 역전파(backpropagation), 잔차 연결(residual connection), 어텐션(attention), LoRA, RAG는 보충이 필요하다. 전통적 ML 두 문항을 맞혔지만, 두 객관식 문항으로 수학·ML 선수 지식이나 직접 구현 능력이 검증된 것은 아니다. 실제 수업의 학습자 코드와 자기 설명으로 추가 확인한다.

## Path

공식 배치 결과: 4/10점은 Phase 3: Deep Learning Core에 대응한다. 공식 상태 규칙을 그대로 적용하면 Phase 0과 2는 Skip, Phase 1은 수학 영역 1/2점이므로 Review, Phase 3–19는 Do다. 공식 경로 합계는 ~1,093시간, 18단계다. 이는 점수 매핑이며 선수 지식의 완전한 숙달을 뜻하지 않는다.

실제 권장 학습 계획: 사용자의 처음부터 학습하려는 목표, Git/API/Docker 기초 부족, 내적 및 딥러닝 개념의 미숙지를 반영해 Phase 0부터 순서대로 진행한다. 모든 단계는 Do로 유지한다. 이것은 공식 배치 규칙 자체를 바꾼 결과가 아니라 사용자의 목표에 맞춘 학습 경로다. 과정을 임의로 생략하지 않으며, 이미 아는 내용은 실행 증거와 이해도 확인을 통해 빠르게 진행한다.

| Phase | Name | Status | Est. hours |
|-------|------|--------|------------|
| 0 | Setup & Tooling | Do | 14 |
| 1 | Math Foundations | Do | 23 |
| 2 | ML Fundamentals | Do | 21 |
| 3 | Deep Learning Core | Do | 15 |
| 4 | Computer Vision | Do | 27 |
| 5 | NLP | Do | 30 |
| 6 | Speech & Audio | Do | 18 |
| 7 | Transformers Deep Dive | Do | 14 |
| 8 | Generative AI | Do | 14 |
| 9 | Reinforcement Learning | Do | 13 |
| 10 | LLMs from Scratch | Do | 26 |
| 11 | LLM Engineering | Do | 19 |
| 12 | Multimodal AI | Do | 65 |
| 13 | Tools & Protocols | Do | 43 |
| 14 | Agent Engineering | Do | 55 |
| 15 | Autonomous Systems | Do | 20 |
| 16 | Multi-Agent & Swarms | Do | 28 |
| 17 | Infrastructure & Production | Do | 32 |
| 18 | Ethics, Safety & Alignment | Do | 31 |
| 19 | Capstone Projects | Do | 620 |

전체 단계 합계: ~1,128시간, 20단계, 523개 수업. ROADMAP 단계 제목의 추정치 기준이며 보충·복습 시간은 별도다. README의 ~342시간 및 ROADMAP 하단 ~1,081시간과 불일치한다. 진도에 맞춰 실제 소요 시간을 조정한다.

학습 운영: 공식 순서와 선수 지식을 우선한다. 설명은 필요한 이유 → 개념 → 명령 → 실행 결과를 연결한다. 새 용어는 등장하기 전에 정의하고 충분히 설명한 뒤 이해 확인을 한다. 짧은 단계별 실습으로 진행하며 설명을 생략한 퀴즈를 먼저 내지 않는다. 설명 → 학습자가 직접 구현·수정 → 실행 및 검증 → 이해도 평가 순서로 한 수업씩 진행한다. Python 함수·자료구조·파일 처리·디버깅, Git, HTTP/API, 도구 기초가 부족하면 해당 수업에서 보충한다. 완성 코드를 대신 작성하지 않고 작은 질문과 힌트를 제공한다. 공식 학습 흐름의 수학 → 직접 구현(Build It) → 라이브러리 비교(Use It) → 결과물(Ship It)을 유지한다.

원본 강의 파일은 수정하지 않는다. 실습 코드는 learning-artifacts/<phase>/<lesson>/ 아래에, 실행 증거·자기 설명도 그곳에 보관한다. 수업 완료 및 실제 이해도 평가 후에만 아래 Progress log에 기록한다. Review queue는 공식 learn 기준(수업 퀴즈 70% 미만)으로 관리한다. 환경 설정이나 튜터가 실행한 데모는 학습자 수료로 계산하지 않는다.

환경 확인: Python 3.12.14, Git 2.52.0, Node 24.19.0; .venv의 NumPy 2.3.5. 공식 beginner preflight 2/2 통과. Docker 서버 28.4.0 응답 확인(컨테이너 실습 미실행). GPU 가용성은 미검증이다. 원격 API 인증·네트워크와 실제 MCP 호스트 연결은 해당 수업에서 확인한다. GPU가 필요하면 작은 CPU 예제 또는 외부 GPU 환경을 사용하고, 로컬 에디터·데스크톱 호스트 실습은 사용자 PC에서 실행할 절차를 제공한다.

공식 스킬: skills/start-learning/SKILL.md 및 skills/find-your-level/SKILL.md를 이 세션에서 직접 읽어 적용했다. Codex의 자동 검색 범위에 start-learning 설치는 확인되지 않았다. Node/npx 및 skills CLI 실행을 확인했으므로 프로젝트 범위 설치를 시도할 수 있다. 자동 등록·현재 세션 재검색 여부는 별도 검증이 필요하다. 공식 설치 절차는 `npx skills add rohitg00/ai-engineering-from-scratch`를 실행하고 Codex 및 프로젝트 범위를 선택하는 것이다. 설치는 아직 수행하지 않았으며 현재는 저장소 스킬 문서를 직접 적용한다. LEARNING.md를 원본 수업과 분리된 개인 학습 상태 파일로 사용한다.

첫 수업 실행 증거 및 보충 기록(2026-10-08):

- 학습자가 check_env.py에 Python 경로·버전, NumPy 버전 및 내적 코드를 작성했다. `np.**version**` 문법 오류를 `np.__version__`으로 직접 수정했다. Python 3.12.14, NumPy 2.3.5, 자기 내적 14 출력 확인; [1,2,4]의 결과 21도 예측·검증했다.
- 학습자가 activation-practice.sh의 세 명령을 작성했다. 같은 셸에서 기본 Python → .venv Python 전환을 확인했고, deactivate 후 기본 Python 복귀도 검증했다. 가상환경은 라이브러리 내부가 아닌 프로젝트의 .venv 폴더라는 점을 보충했다.
- 공식 beginner preflight 필수 Python/Git 2/2 통과. --show-later에서 Node/npx/NumPy를 확인했다. Matplotlib/Jupyter는 미설치이고 초급 경로 필수 항목이 아니다.
- uv 0.12.19 사용 확인. 기본 캐시 디렉터리 쓰기 실패는 `--cache-dir /tmp/ai-course-uv-cache`로 해결했다. 필요하면 같은 옵션으로 쓰기 가능한 캐시를 지정한다.
- CPU PyTorch 2.14.1+cpu 설치 및 의존성 검사 통과. 학습자가 check_torch.py를 작성해 `tensor([1, 2, 3]) tensor(14)` 출력과 종료 코드 0 확인. CUDA/MPS는 모두 False. 이는 현재 설치 환경에서 사용 불가라는 뜻이며 물리 GPU 전체를 조사한 결과는 아니다.
- Python hello.py, JavaScript hello.js, Rust hello.rs 모두 학습자 작성 및 Hello, AI Engineering! 출력 확인. Rust의 printIn!/printin! 오타를 println!으로 수정했고 컴파일·실행 모두 성공했다. 생성 실행 파일은 /tmp에 두며 GitHub에 올리지 않는다.
- Rust 도구 위치: /workspace/ai-course-tools/cargo 및 /workspace/ai-course-tools/rustup. rustc/cargo 1.99.0 실행 확인. 새 셸에서 RUSTUP_HOME=/workspace/ai-course-tools/rustup, CARGO_HOME=/workspace/ai-course-tools/cargo를 지정하고 /workspace/ai-course-tools/cargo/bin을 PATH에 추가해야 한다. 새 환경에는 도구가 자동 복원된다고 가정하지 말고 확인한다.
- 공식 post 퀴즈 응답 B, C, B: 3/3점. uv 설명 누락으로 두 번째 문항을 중단했다가 충분히 설명한 뒤 재개했다.
- 처음에 연습 문제를 임의로 확장 항목으로 분류하고 성급히 완료 처리했던 판단을 정정했다. PyTorch 설치와 네 언어 Hello World는 공식 Exercises에 포함된다. Julia 설치는 Optional, GPU 설정은 If You Have One으로 명시되어 있으므로 Julia/GPU 미수행을 구분한다. Python/JavaScript/Rust 및 CPU PyTorch 실습을 마친 상태로 기록한다.

저장 범위: LEARNING.md와 learning-artifacts/의 개인 실습 소스만 GitHub에 보관한다. 원본 강의·테스트·의존성 선언은 수정하지 않는다. .venv와 설치된 도구, 임시 실행 파일은 Git 커밋 대상이 아니며 새 실행 환경에서 준비 상태를 별도로 확인해야 한다.

## Progress log

| Date | Lesson | Quiz | Note |
|------|--------|------|------|
| 2026-10-08 | 00-setup-and-tooling/01-dev-environment | 3/3 | Python/NumPy 점검·내적, activate/deactivate, Python/JavaScript/Rust Hello World, CPU PyTorch 텐서·내적 실습 완료. Julia 선택 실습 보류, GPU 백엔드 사용 불가로 실제 GPU 계산 미수행. |

## Review queue
