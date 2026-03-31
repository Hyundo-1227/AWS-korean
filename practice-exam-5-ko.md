---
layout: exam
---

# 연습 시험 5

1. 한 회사가 AWS에서 EC2 인스턴스로 자사의 전자상거래 사이트를 운영하고 있습니다. 사이트가 사용 불가능해지면, 사이트가 중단된 매 분마다 회사는 큰 금액을 잃게 됩니다. 이때 어떤 설계 원칙을 사용해 장애(outage) 위험을 최소화해야 합니까?
    - A. 최소 권한(Least Privilege).
    - B. 파일럿 라이트(Pilot Light).
    - C. 내결함성(Fault Tolerance).
    - D. 멀티스레딩(Multi-threading).

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

2. 1년 기간으로 예약 인스턴스(Reserved instance)를 구매하기로 결정했습니다. 어떤 옵션이 가장 큰 총 할인(total discount)을 제공합니까?
    - A. 전액 선결제(All up-front reservation).
    - B. 예약 인스턴스 결제 옵션은 모두 동일한 할인 수준을 제공합니다.
    - C. 부분 선결제(Partial up-front reservation).
    - D. 선결제 없음(No up-front reservation).

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

3. AWS는 클라우드에서 데이터를 보호하기 위해 어떤 기능을 제공합니까? (두 개 선택)
    - A. 액세스 제어.
    - B. 물리적 MFA 장치.
    - C. 데이터 암호화.
    - D. 무제한 스토리지.
    - E. 로드 밸런싱.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, C
    </details>

4. 한 AWS 고객이 Amazon Linux 인스턴스를 2시간 5분 9초 동안 사용했고, CentOS 인스턴스를 4시간 23분 7초 동안 사용했습니다. 고객은 총 얼마나 과금됩니까?
    - A. 리눅스 인스턴스는 3시간, CentOS 인스턴스는 5시간입니다.
    - B. 리눅스 인스턴스는 2시간 5분 9초, CentOS 인스턴스는 4시간 23분 7초입니다.
    - C. 리눅스 인스턴스는 2시간 5분 9초, CentOS 인스턴스는 5시간입니다.
    - D. 리눅스 인스턴스는 3시간, CentOS 인스턴스는 4시간 23분 7초입니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C

      Explanation:
      - 각 인스턴스별로, 인스턴스가 시작(런치)된 시점부터 종료 또는 정지될 때까지, 사용한 인스턴스-시간(instance-hour) 단위로 과금됩니다.
      - 사용한 인스턴스의 일부 시간(partial instance-hour)은 Linux, Windows, Windows with SQL Enterprise, Windows with SQL Standard, Windows with SQL Web 인스턴스에 대해서는 초 단위로 과금되며, 그 외 모든 인스턴스 타입은 전체 1시간 단위로 과금됩니다.
    </details>

5. 고객이 지원 티켓(support cases)을 프로그래밍 방식으로 관리할 수 있게 해주는 AWS 지원 기능은 무엇입니까?
    - A. AWS Trusted Advisor.
    - B. AWS Operations Support.
    - C. AWS Support API.
    - D. AWS Personal Health Dashboard.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

6. 고객이 AWS Identity and Access Management(IAM)과 상호작용하기 위해 사용할 수 있는 방법은 무엇입니까? (두 개 선택)
    - A. AWS CLI.
    - B. AWS Security Groups.
    - C. AWS SDKs.
    - D. AWS Network Access Control Lists.
    - E. AWS CodeCommit.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, C
    </details>

7. 다음 중 AWS Identity and Access Management(IAM) ID의 유형은 무엇입니까? (두 개 선택)
    - A. AWS Resource Groups.
    - B. IAM Policies.
    - C. IAM Roles.
    - D. IAM Users.
    - E. AWS Organizations.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C, D
    </details>

8. 다음 중 Amazon RDS의 기능 중에서, 데이터베이스의 읽기(read) 활동을 오프로딩(offloading)하는 데 도움이 되는 것은 무엇입니까?
    - A. Database Snapshots.
    - B. Multi-AZ Deployments.
    - C. Automatic Backups.
    - D. Read Replicas.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

9. AWS는 AWS 서비스와 관련된 보안 및 개인정보 보호 이벤트에 대해 고객에게 어떻게 알립니까?
    - A. AWS ACM 서비스를 사용합니다.
    - B. Security Bulletins를 사용합니다.
    - C. AWS Management Console을 사용합니다.
    - D. Compliance Resources를 사용합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

10. 일시적인(temporary) 액세스를 AWS 리소스에 부여할 때 가장 적합한 IAM 엔티티는 무엇입니까?
    - A. IAM Users.
    - B. Key Pair.
    - C. IAM Roles.
    - D. IAM Groups.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

11. 한 회사에는 단일 EC2 인스턴스에서 호스팅되는 웹 애플리케이션이 있으며, 피크 시간대에 CPU Utilization이 거의 100%에 가까워지고 있습니다. 서버를 수직으로(vertically) 스케일하는 대신, 회사는 동일한 방식으로 EC2 인스턴스 3개를 병렬로 배포하고 세 서버로 트래픽을 분산하기로 했습니다. 트래픽을 고르게 분산하려면 회사는 어떤 AWS 서비스를 사용해야 합니까?
    - A. AWS Global Accelerator.
    - B. AWS Application Load Balancer (ALB).
    - C. Amazon CloudFront.
    - D. Transit VPC.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

12. 다음 중 어떤 접근 방식이 사람의 실수(human error)를 없애고, AWS 환경을 생성/업데이트하는 과정을 자동화하는 데 도움이 됩니까?
    - A. 소프트웨어 테스트 자동화 도구를 사용합니다.
    - B. AWS CodeDeploy를 사용해 AWS 환경을 구축하고 자동화합니다.
    - C. 코드를 사용해 AWS 인프라를 프로비저닝하고 운영합니다.
    - D. 모든 애플리케이션을 전용 호스트(dedicated host)로 마이그레이션합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

13. 회사가 AWS 계정을 승인되지 않은 액세스로부터 더 안전하게 보호하려고 합니다. 다음 중 어떤 옵션이 이 목표를 달성할 수 있습니까?
    - A. SDK나 CLI를 통해 이루어지는 모든 API 호출을 제한합니다.
    - B. 회사의 각 부서(개발, QA, 운영)를 위해 IAM 계정을 1개씩 만들고, 해당 부서의 모든 직원이 이를 공유합니다.
    - C. 모든 IAM User의 액세스에 대해 Multi-Factor Authentication(MFA)를 요구합니다.
    - D. 로그인 비밀번호를 두 개 설정합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

14. AWS 서비스는 사용(usage)에 기반해 볼륨 할인(volume discounts)을 제공합니까?
    - A. Amazon VPC.
    - B. Amazon S3.
    - C. Amazon Lightsail.
    - D. AWS Cost Explorer.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

15. AWS 리소스가 배포될 리전을 결정할 때 고려해야 하는 요소는 무엇입니까? (두 개 선택)
    - A. AWS 리전의 보안 수준.
    - B. 데이터 주권(data sovereignty).
    - C. 비용(cost).
    - D. 계획된 VPC 개수.
    - E. 회사 위치에 대한 지리적 근접성.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B, C
    </details>

16. 사용 중인 AWS에서 재무 서비스 웹 애플리케이션이 있고, 데이터는 MySQL 데이터베이스에 저장됩니다. 다음 중 빠른 인메모리 캐시에서 정보를 검색할 수 있게 해 애플리케이션 성능을 향상시키는 AWS 서비스는 무엇입니까?
    - A. Amazon EFS.
    - B. Amazon Neptune.
    - C. Amazon ElastiCache.
    - D. DAX.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

17. EC2 인스턴스에 대해 Auto Scaling Groups을 사용하는 이점은 무엇입니까?
    - A. Auto Scaling Groups는 지연을 줄이고 성능을 향상시키기 위해 전 세계 엣지 위치에 가장 최근 응답을 캐시합니다.
    - B. Auto Scaling Groups는 애플리케이션 가용성과 내결함성을 높이기 위해 여러 가용 영역에 걸쳐 EC2 인스턴스를 스케일합니다.
    - C. Auto Scaling Groups는 글로벌 사용자에 대한 지연을 줄이기 위해 여러 리전에 걸쳐 EC2 인스턴스를 스케일합니다.
    - D. Auto Scaling Groups는 성능을 향상시키기 위해 여러 가용 영역에 걸쳐 애플리케이션 트래픽을 분산합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

18. 최근 몇 년 동안 AWS 인프라와 전통적 인프라 간 TCO 격차가 더 벌어졌습니다. 그 이유로 다음 중 어떤 것이 가능합니까?
    - A. AWS는 고객이 자본 지출(capital expenditures)에 더 투자하도록 돕습니다.
    - B. AWS는 인프라 운영의 모든 작업을 자동화하므로 고객은 인력 비용에 더 많이 절감할 수 있습니다.
    - C. AWS는 고객에게 클라우드 컴퓨팅 비용을 계속해서 낮추고 있습니다.
    - D. AWS는 추가 비용 없이 AWS 리소스를 보호합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

19. 다음 중 “클라우드에서의 보안(security IN the cloud)”을 구현하기 위한 고객의 책임에 해당하는 것은 무엇입니까? (두 개 선택)
    - A. 애플리케이션을 위한 스키마를 구축합니다.
    - B. 물리 하드웨어를 교체합니다.
    - C. 새로운 하이퍼바이저를 생성합니다.
    - D. 기반 인프라의 패치 관리를 수행합니다.
    - E. 파일 시스템 암호화를 합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, E
    </details>

20. 고객이 AWS 리소스를 보호하기 위해 사용할 수 있는 MFA 장치의 한 유형은 무엇입니까?
    - A. AWS CloudHSM.
    - B. U2F Security Key.
    - C. AWS Access Keys.
    - D. AWS Key Pair.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

21. 한 회사가 가능한 한 빠르게 기존 .NET 애플리케이션을 AWS에 배포하려고 합니다. 고객은 이 목표를 달성하기 위해 어떤 AWS 서비스를 사용해야 합니까?
    - A. Amazon SNS.
    - B. AWS Elastic Beanstalk.
    - C. AWS Systems Manager.
    - D. AWS Trusted Advisor.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

22. 다음 중 Amazon EC2 비용을 추정할 때 고려하지 않는 요소는 무엇입니까? (두 개 선택)
    - A. 인스턴스가 실행될 시간의 양.
    - B. 보안 그룹의 개수.
    - C. 할당된 Elastic IP 주소.
    - D. Hosted Zones의 개수.
    - E. 인스턴스의 개수.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B, D
    </details>

23. 다음 중 AWS에서 엔터프라이즈가 온프레미스 스토리지를 비용 효율적으로 AWS로 확장하는 데 도움이 되는 AWS 서비스는 무엇입니까?
    - A. AWS Data Pipeline.
    - B. AWS Storage Gateway.
    - C. Amazon Aurora.
    - D. Amazon EFS.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

24. 한 회사가 온라인 클라우드 스토리지 플랫폼을 구축하고 있습니다. 용량을 자동으로 확장할 수 있으면서도 비용을 최소화하는 스토리지 서비스를 사용해야 합니다. 이 요구 사항을 충족하기 위해 어떤 AWS 스토리지 서비스를 사용해야 합니까?
    - A. Amazon Simple Storage Service.
    - B. Amazon Elastic Block Store.
    - C. Amazon Elastic Container Service.
    - D. AWS Storage Gateway.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

25. 숙련된 시스템 관리자(sys-admin)를 팀에 고용했습니다. 평소처럼 그가 AWS 서비스와 상호작용할 수 있도록 새로운 IAM 사용자를 만들었습니다. 첫날, 그에게 기존의 모든 Amazon EBS 볼륨의 스냅샷을 생성하고, 이를 새 Amazon S3 버킷에 저장하라고 시켰습니다. 그런데 새 멤버가 EBS 스냅샷이나 S3 버킷을 생성할 수 없다고 보고합니다. 무엇이 그를 막고 있을 수 있습니까?
    - A. EBS와 S3는 루트 계정(root account) 소유자에게만 접근 가능합니다.
    - B. 시스템 관리자는 새 IAM 계정을 활성화하기 위해 먼저 AWS Support에 연락해야 합니다.
    - C. 스냅샷을 저장하기 위한 S3 공간이 충분하지 않습니다.
    - D. 모든 새 사용자에게 비명시적(non-explicit) deny가 적용되어 있습니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

26. 외부 감사자가 회사 계정의 AWS 리소스에 대한 모든 액세스 기록(log)을 요청하고 있습니다. 다음 중 감사자가 요청한 정보를 제공해주는 서비스는 무엇입니까?
    - A. AWS CloudTrail.
    - B. Amazon CloudFront.
    - C. AWS CloudFormation.
    - D. Amazon CloudWatch.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

27. 다음 중 Amazon Cloud Directory에 대해 옳은 것은 무엇입니까?
    - A. Amazon Cloud Directory는 여러 차원에서 데이터 계층 구조를 정리할 수 있게 해줍니다.
    - B. Amazon Cloud Directory는 비디오와 데이터 스트림을 실시간으로 분석할 수 있게 해줍니다.
    - C. Amazon Cloud Directory는 기존 Active Directory 자격 증명으로 AWS에 접속할 수 있게 해줍니다.
    - D. Amazon Cloud Directory는 도메인 이름을 등록하고 관리할 수 있게 합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

28. 한 사용자가 프로덕션 시스템 장애로 인해 AWS Support에서 도움을 받기 위해 “Production System Down” 지원 케이스를 열었습니다. 이러한 유형의 지원 케이스에 대한 예상 응답 시간은 얼마입니까?
    - A. 12시간.
    - B. 15분.
    - C. 24시간.
    - D. 1시간.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

29. AWS에서 애플리케이션을 고가용(highly available)하게 만들기 위한 모범 사례는 무엇입니까?
    - A. 애플리케이션을 최소 두 개의 가용 영역(Availability Zones)에 배포합니다.
    - B. 여러 AWS 리전에 걸쳐 Elastic Load Balancing(ELB)를 사용합니다.
    - C. 동일 가용 영역 내에서 최소 두 대의 서버에 애플리케이션 코드를 배포합니다.
    - D. 모든 들어오는 요청을 처리하도록 애플리케이션 코드를 다시 작성합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

30. AWS에서 애플리케이션을 실행하는 비용과 온프레미스에서 실행하는 비용을 비교하는 TCO 분석을 수행할 때 고려해야 하는 것은 무엇입니까? (두 개 선택)
    - A. 인건비 및 IT 비용.
    - B. 냉각 및 전력 소비.
    - C. Amazon EBS 컴퓨팅 파워.
    - D. 소프트웨어 아키텍처.
    - E. 소프트웨어 호환성.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, B
    </details>

31. 회사의 비즈니스 핵심 시스템이 AWS에서 호스팅되고 있으며, 장애가 발생하면 지원 상호작용에 대한 응답 시간이 15분 미만이어야 합니다. 이 회사는 어떤 AWS Support 플랜을 사용해야 합니까?
    - A. AWS Basic Support.
    - B. AWS Developer Support.
    - C. AWS Business Support.
    - D. AWS Enterprise Support.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

32. 다음 중 AWS의 어떤 제공 항목들이 서버리스 서비스입니까? (두 개 선택)
    - A. Amazon EC2.
    - B. AWS Lambda.
    - C. Amazon DynamoDB.
    - D. Amazon EMR.
    - E. Amazon RDS.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B, C
    </details>

33. AWS에서 빠르게 SSL/TLS 인증서를 구매하고 배포할 수 있게 해주는 AWS 서비스는 무엇입니까?
    - A. Amazon GuardDuty.
    - B. AWS ACM.
    - C. Amazon Detective.
    - D. AWS WAF.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

34. Chef와의 통합을 제공하여 EC2 인스턴스 설정을 자동화하는 AWS 서비스는 무엇입니까?
    - A. AWS Config.
    - B. AWS OpsWorks.
    - C. AutoScaling.
    - D. AWS CloudFormation.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

35. 한 고객이 AWS 환경에서 객체를 저장하고, 인터넷을 통해 다운로드할 수 있게 하려고 합니다. 이를 수행할 수 있는 AWS 서비스는 무엇입니까?
    - A. Amazon EBS.
    - B. Amazon EFS.
    - C. Amazon S3.
    - D. Amazon Instance Store.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

36. 다음 중 Amazon CloudFront로 전달되는 HTTP 및 HTTPS 요청을 모니터링하는 데 사용할 수 있는 서비스는 무엇입니까?
    - A. AWS WAF.
    - B. Amazon CloudWatch.
    - C. AWS Cloud9.
    - D. AWS CloudTrail.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

37. 한 회사가 웹 애플리케이션을 AWS로 마이그레이션하고 있습니다. 애플리케이션의 컴퓨트 용량은 연중 내내 계속 사용됩니다. 아래 옵션 중 이 회사에 가장 비용 효율적인 솔루션을 제공하는 것은 무엇입니까?
    - A. 온디맨드 인스턴스(On-demand Instances).
    - B. 전용 호스트(Dedicated Hosts).
    - C. 스팟 인스턴스(Spot Instances).
    - D. 예약 인스턴스(Reserved Instances).

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

38. 한 회사는 Amazon DynamoDB 데이터베이스를 관리하기 위해 새 직원에게 장기 액세스를 제공하려고 합니다. 다음 중 이러한 권한을 부여할 때 권장되는 모범 사례는 무엇입니까?
    - A. IAM role을 만들고, Amazon DynamoDB 접근 권한이 있는 policy를 연결합니다.
    - B. IAM role을 만들고, Administrator 권한이 있는 policy를 연결합니다.
    - C. IAM user를 만들고, Amazon DynamoDB 접근 권한이 있는 policy를 연결합니다.
    - D. IAM user를 만들고, Administrator 권한이 있는 policy를 연결합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

39. Amazon EC2 인스턴스에서 실행되는 애플리케이션에 권한을 부여할 때, 다음 중 모범 사례로 간주되는 것은 무엇입니까?
    - A. 권한을 위임할 때마다 새 IAM 액세스 키를 생성합니다.
    - B. 필요한 AWS 자격 증명을 애플리케이션 코드 안에 직접 저장합니다.
    - C. 장기(long-term) 액세스 키 대신 임시 보안 자격 증명(temporary security credentials, IAM roles)을 사용합니다.
    - D. 아무 것도 하지 않습니다. Amazon EC2 인스턴스에서 실행되는 애플리케이션은 다른 AWS 서비스나 리소스와 상호작용할 권한이 필요하지 않습니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

40. 다음 중 워크로드를 AWS로 마이그레이션할 때 고객이 비용을 절감하는 데 도움이 되는 것은 무엇입니까?
    - A. 관리형 서비스 대신 서버를 사용합니다.
    - B. AWS에서 기존 서드파티 소프트웨어 라이선스를 사용합니다.
    - C. 프로덕션 워크로드를 AWS Regions 대신 AWS edge locations로 마이그레이션합니다.
    - D. 모든 워크로드를 비용 최적화된 환경에서 실행하기 위해 AWS Outposts를 사용합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

41. 단일(monolithic) 기반 아키텍처로 설계된 레거시 애플리케이션이 있습니다. 이 애플리케이션의 구성 요소를 디커플링(decouple)하려면 어떤 AWS 서비스를 사용할 수 있습니까?
    - A. Amazon SQS.
    - B. Virtual Private Gateway.
    - C. AWS Artifact.
    - D. Amazon CloudFront.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

42. Virtual Multi-Factor Authentication을 활성화하기 위해 사용할 수 있는 것은 무엇입니까? (두 개 선택)
    - A. Amazon Connect.
    - B. AWS CLI.
    - C. AWS Identity and Access Management (IAM).
    - D. Amazon SNS.
    - E. Amazon Virtual Private Cloud.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B, C
    </details>

43. 모범 사례에 따르면, 대량의 바이너리 파일을 처리하기에 가장 적절한 것은 무엇입니까?
    - A. EC2 인스턴스를 수직 스케일링(vertically scaling)합니다.
    - B. RDS 인스턴스를 병렬로 실행합니다.
    - C. RDS 인스턴스를 수직 스케일링(vertically scaling)합니다.
    - D. EC2 인스턴스를 병렬로 실행합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

44. 한 회사가 전 세계적으로 비디오 강의를 배포하기 위해 Amazon S3와 Amazon CloudFront를 사용하려고 합니다. 이 서비스들의 비용을 추정하기 위해 회사는 어떤 도구를 사용할 수 있습니까?
    - A. AWS Cost Explorer.
    - B. AWS Pricing Calculator.
    - C. AWS Budgets.
    - D. AWS Cost & Usage Report.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

45. AWS Management Console에서 본인이 만들지 않았다고 생각되는 리소스가 보이면 어떻게 해야 합니까? (두 개 선택)
    - A. 실행 중인 모든 서비스를 중지하고 조사를 시작합니다.
    - B. 루트 계정(root account) 비밀번호를 AWS Support에 제공해 트러블슈팅과 계정 보안에 도움을 받습니다.
    - C. AWS CloudTrail 로그를 확인하고, 해당 리소스에 접근 권한이 있는 모든 IAM 사용자를 삭제합니다.
    - D. 조사를 열고 잠재적으로 손상(compromised)되었을 수 있는 IAM 사용자들을 삭제합니다.
    - E. AWS 루트 계정 비밀번호와 IAM 사용자들의 비밀번호를 변경합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D, E
    </details>

46. AWS에서 솔루션을 설계할 때 핵심 관행 중 하나는 구성 요소 간 의존성을 최소화해, 단 하나의 구성 요소 장애가 다른 구성 요소에 영향을 주지 않도록 하는 것입니다. 이 관행을 무엇이라고 합니까?
    - A. Elastic coupling.
    - B. Loosely coupling.
    - C. Scalable coupling.
    - D. Tightly coupling.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

47. 다음 중 여러 EC2 인스턴스가 동시에 마운트할 수 있는 NFS 파일 시스템을 제공하는 AWS 서비스는 무엇입니까?
    - A. Amazon Elastic File System.
    - B. Amazon Simple Storage Service.
    - C. Amazon Elastic Block Store.
    - D. AWS Storage Gateway.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

48. 한 리전(Region) 내 가용 영역(Availability Zones)은 낮은 지연 시간 링크로 연결되어 있습니다. 이 링크의 이점은 무엇입니까?
    - A. 데이터 센터로의 프라이빗 연결을 만듭니다.
    - B. 글로벌 수준의 고가용성을 달성합니다.
    - C. 새 컴퓨트 리소스를 프로비저닝하는 과정을 자동화합니다.
    - D. 데이터의 동기(synchronous) 복제를 가능하게 합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

49. 다음 중 AWS Lambda에서 지원하는 언어에 대해 옳은 것은 무엇입니까? (두 개 선택)
    - A. Lambda는 Python과 Node.js만 지원하지만, 다른 언어의 코드를 이 형식으로 변환하기 위한 서드파티 플러그인을 사용할 수 있습니다.
    - B. Lambda는 Node.js, Python, Java 같은 여러 프로그래밍 언어를 기본(native)으로 지원합니다.
    - C. Lambda는 AWS의 독점 프로그래밍 언어로, 마이크로서비스를 위한 용도입니다.
    - D. Lambda는 프로그래밍 언어를 지원하지 않습니다. 이는 서버리스 컴퓨트 서비스입니다.
    - E. Lambda는 API를 통해 어떤 프로그래밍 언어든 지원할 수 있습니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B, E
    </details>

50. AWS X-Ray의 기능은 무엇입니까? (두 개 선택)
    - A. 애플리케이션 구성 요소를 자동으로 디커플링합니다.
    - B. 사용자 요청을 추적해 애플리케이션 문제를 식별하는 데 도움이 됩니다.
    - C. 애플리케이션 성능 개선에 도움이 됩니다.
    - D. 애플리케이션을 Amazon EC2 인스턴스에 배포합니다.
    - E. 애플리케이션을 온프레미스 서버에 배포합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B, C
    </details>

