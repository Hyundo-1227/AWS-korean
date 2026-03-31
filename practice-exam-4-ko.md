---
layout: exam
---

# 연습 시험 4

1. 개발자가 고객의 eCommerce 웹사이트에서 HTTPS 프로토콜을 사용하기 위해 SSL 보안 인증서를 설정해야 합니다. 다음 중 필요한 SSL 서버 인증서를 배포하는 데 사용할 수 있는 AWS 서비스는 무엇입니까? (두 개 선택)
    - A. Amazon Route 53.
    - B. AWS ACM.
    - C. AWS Directory Service.
    - D. AWS Identity & Access Management.
    - E. AWS Data Pipeline.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, B
    </details>

2. 다음 중 여러분의 개입 없이 자동으로 스케일하는 AWS 서비스는 무엇입니까? (두 개 선택)
    - A. Amazon EC2.
    - B. Amazon S3.
    - C. AWS Lambda.
    - D. Amazon EMR.
    - E. Amazon EBS.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B, C
    </details>

3. 한 회사가 서버리스 아키텍처를 사용하기 위해 Amazon EC2에서 AWS Lambda로 애플리케이션을 마이그레이션하려고 합니다. 다음 중 마이그레이션 이후 AWS의 책임이 되는 것은 무엇입니까? (두 개)
    - A. 애플리케이션 관리.
    - B. 용량 관리.
    - C. 액세스 제어.
    - D. 운영 체제 유지보수.
    - E. 데이터 관리.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B, D
    </details>

4. ELB(Elastic Load Balancer)는 어떻게 애플리케이션의 신뢰성을 향상시킵니까?
    - A. 여러 S3 버킷에 트래픽을 분산합니다.
    - B. 데이터를 여러 가용 영역에 복제합니다.
    - C. 데이터베이스 Read Replicas를 생성합니다.
    - D. 정상(healthy) 대상에게만 트래픽이 전달되도록 보장합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

5. 한 회사가 온프레미스에서 AWS로 웹사이트를 마이그레이션해야 합니다. 보안이 매우 중요하므로, 다른 AWS 고객과 공유되지 않는 하드웨어에 웹사이트를 호스팅해야 합니다. 다음 중 어떤 EC2 인스턴스 옵션이 이 요구 사항을 충족합니까?
    - A. 온디맨드 인스턴스.
    - B. 스팟 인스턴스.
    - C. 전용 인스턴스.
    - D. 예약 인스턴스.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

6. 고객이 수십억 개의 이미지와 비디오를 Amazon S3에 저장하려고 합니다. 고객은 약 60페타바이트(PB)의 데이터를 옮겨야 합니다. 다음 중 이 데이터를 AWS로 전송하는 데 가장 적합한 선택은 무엇입니까?
    - A. Snowball.
    - B. S3 Transfer Acceleration.
    - C. Snowmobile.
    - D. Amazon VPC.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

7. 한 회사가 대량의 보관(archived) 데이터를 AWS로 마이그레이션하려고 합니다. 보관 데이터는 5년 동안 유지되어야 하며, 요청 후 5시간 내에 검색(복구)할 수 있어야 합니다. 사용하기 가장 비용 효율적인 AWS 스토리지 서비스는 무엇입니까?
    - A. Amazon S3 Glacier.
    - B. Amazon EFS.
    - C. Amazon S3 Standard.
    - D. Amazon EBS.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

8. 사용자 권한을 관리하는 데 사용되는 AWS 서비스는 무엇입니까?
    - A. Security Groups.
    - B. Amazon ECS.
    - C. AWS IAM.
    - D. AWS Support.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

9. 다음 중 어떤 지원 플랜에 AWS Support Concierge Service가 포함됩니까?
    - A. Premium Support.
    - B. Business Support.
    - C. Enterprise Support.
    - D. Standard Support.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

10. 한 회사가 API 호출 이력(API call history)을 사용해 리소스 변경 사항을 추적하려고 합니다. 이를 달성하는 데 도움이 되는 AWS 서비스는 무엇입니까?
    - A. AWS Config.
    - B. Amazon CloudWatch.
    - C. AWS CloudTrail.
    - D. AWS CloudFormation.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

11. AWS 관리형(managed) 서비스 사용의 장점은 무엇입니까? (두 개 선택)
    - A. 가상 인프라에 대한 완전한 제어를 제공합니다.
    - B. 고객이 새로운 솔루션을 더 빠르게 제공할 수 있게 합니다.
    - C. 운영 복잡도를 낮춥니다.
    - D. 데이터를 암호화할 필요를 없애줍니다.
    - E. 개발자가 패치 관련 활동을 모두 제어할 수 있게 합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B, C
    </details>

12. 다음 중 Amazon S3의 사용 사례는 무엇입니까? (두 개 선택)
    - A. 정적 웹사이트 호스팅.
    - B. 지속적으로 높은 CPU 사용률이 필요한 웹사이트 호스팅.
    - C. 비용 효율적인 데이터베이스 및 로그 저장.
    - D. CloudFront 서비스용 미디어 저장소.
    - E. 어떤 규모에서든 데이터 스트림 처리.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, D
    </details>

13. AWS는 액세스 키(access keys)에 대해 어떤 권장 사항을 제시합니까?
    - A. 모든 액세스 키를 삭제하고 비밀번호를 대신 사용합니다.
    - B. 신뢰할 수 있는 사람에게만 공유합니다.
    - C. 정기적으로 회전(rotate)합니다.
    - D. 애플리케이션 코드 안에 저장합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

14. 사용자 이름과 비밀번호 인증 위에 추가적인 보안 계층을 제공하는 AWS IAM 기능은 무엇입니까?
    - A. Key Pair.
    - B. Access Keys.
    - C. SDK.
    - D. MFA.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

15. AWS 서비스에 접근하기 위해 API를 사용하는 이점은 무엇입니까?
    - A. AWS 리소스의 성능을 향상시킵니다.
    - B. AWS 리소스를 프로비저닝하는 데 필요한 시간을 줄입니다.
    - C. 필요한 개발자 수를 줄입니다.
    - D. AWS 리소스를 프로그램적으로 관리할 수 있게 해줍니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

16. 한 회사가 읽기/쓰기 활동이 높은(high read/write activity) 데이터베이스를 AWS로 마이그레이션하려고 합니다. 어떤 스토리지 옵션이 가장 적합합니까?
    - A. AWS Storage Gateway.
    - B. Amazon S3.
    - C. Amazon EBS.
    - D. Amazon Glacier.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

17. AWS 고객은 활용도가 낮은 예약 인스턴스(Reserved instances)를 추적하고, 과도한 지출을 피하려면 어떻게 해야 합니까?
    - A. 모든 AWS 계정을 AWS Organization에 추가하고, Consolidated Billing을 활성화한 뒤 Reserved Instance 공유를 중지합니다.
    - B. Amazon Neptune을 사용해 사용 패턴을 추적/분석하고 활용도가 낮은 예약 인스턴스를 감지한 다음 Amazon EC2 Reserved Instance Marketplace에서 판매합니다.
    - C. AWS Budgets 서비스를 사용해 예약 인스턴스 사용량을 추적하고, 정의한 임계값보다 활용도가 떨어지면 알림 알림(notification) 세트를 구성합니다.
    - D. Amazon CloudTrail을 사용해 사용되지 않는 예약을 자동으로 확인하고 청구서를 줄이는 권장 사항을 얻습니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

18. AWS 서비스 중 표준 MySQL 데이터베이스보다 5배 성능을 제공하는 것은 무엇입니까?
    - A. Amazon Aurora.
    - B. Amazon Redshift.
    - C. Amazon DynamoDB.
    - D. Amazon Neptune.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

19. AWS Service Catalog는 무엇을 제공합니까?
    - A. 고객이 AWS 서비스에 대한 설명과 사용 사례를 빠르게 찾도록 돕습니다.
    - B. 고객이 다양한 AWS 서비스 카탈로그를 탐색할 수 있게 합니다.
    - C. 자주 배포되는 IT 서비스를 구성하고 거버넌스(관리)하는 것을 간단하게 합니다.
    - D. 개발자가 익숙한 프로그래밍 언어를 사용해 AWS에 인프라를 배포할 수 있게 합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

20. Amazon DynamoDB 같은 관리형 서비스(managed services)의 경우, 다음 중 AWS가 책임지는 것은 무엇입니까? (두 개 선택)
    - A. 자격 증명(credentials) 보호.
    - B. 로그인(접근) 활동 로깅.
    - C. 데이터베이스 소프트웨어 패치.
    - D. 운영 체제 유지보수.
    - E. 접근 정책 생성.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C, D
    </details>

21. 다음 중 AWS 클라우드로 애플리케이션 마이그레이션을 계획하는 데 도움이 되는 AWS 서비스는 무엇입니까?
    - A. AWS Snowball Migration Service.
    - B. AWS Application Discovery Service.
    - C. AWS DMS.
    - D. AWS Migration Hub.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

22. 회사가 최근 AWS 계정에 적용된 비용을 분석하려고 합니다. 다음 중 AWS 비용 및 사용량에 대해 가장 세부적인 데이터를 제공하는 것은 무엇입니까?
    - A. Amazon Machine Image.
    - B. AWS Cost Explorer.
    - C. AWS Cost & Usage Report.
    - D. Amazon CloudWatch.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

23. AWS 리전(region)이라는 개념을 가장 잘 설명하는 것은 무엇입니까?
    - A. AWS 리전은 지리적 위치이며 여러 Edge locations의 집합입니다.
    - B. AWS 리전은 단일 AWS 고객만을 위한 전용 가상 네트워크입니다.
    - C. AWS 리전은 지리적 위치이며 여러 가용 영역(Availability Zones)의 집합입니다.
    - D. AWS 리전은 AWS 인프라가 존재하는 국가를 의미합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

24. 한 회사는 여러 S3 버킷이 삭제된 것을 발견했지만, 누가 버킷을 삭제했는지는 불명확합니다. 회사는 다음 중 삭제한 주체의 신원을 파악하기 위해 무엇을 사용할 수 있습니까?
    - A. SNS logs.
    - B. SQS logs.
    - C. CloudWatch Logs.
    - D. CloudTrail logs.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

25. 다음 중 특정 워크로드에 사용할 적절한 데이터베이스 기술을 결정할 때 고려해야 하는 요소는 무엇입니까? (두 개 선택)
    - A. 가용 영역(Availability Zones).
    - B. 데이터 주권(data sovereignty).
    - C. 초당 읽기/쓰기 횟수.
    - D. 쿼리의 성격(nature of the queries).
    - E. 소프트웨어 버그.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C, D
    </details>

26. AWS 리소스에 태깅(tagging) 전략을 적용하는 것의 이점은 무엇입니까? (두 개 선택)
    - A. 특정 프로젝트에 속한 리소스를 빠르게 식별합니다.
    - B. AWS에서 소프트웨어 솔루션을 빠르게 식별합니다.
    - C. AWS 계정에서 API 호출을 추적합니다.
    - D. 삭제된 리소스와 그 메타데이터를 빠르게 식별합니다.
    - E. 여러 리소스에 걸쳐 AWS 지출을 추적합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, E
    </details>

27. AWS 공유 컨트롤(shared controls)은 무엇입니까?
    - A. AWS 서비스 내에서 애플리케이션을 배포하는 방식에 따라 고객이 단독으로 책임져야 하는 컨트롤입니다.
    - B. 고객이 AWS로부터 상속(inherits)받는 컨트롤입니다.
    - C. 인프라 계층과 고객 계층 모두에 적용되는 컨트롤입니다.
    - D. 고객과 AWS가 협력해서 인프라를 보안하기 위해 함께 사용하는 컨트롤입니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

28. AWS에서 성능 효율(performance efficiency)과 관련된 설계 원칙은 무엇입니까? (두 개 선택)
    - A. 전 세계 고객을 더 잘 지원하기 위해 멀티 리전 아키텍처를 구축합니다.
    - B. 모든 계층에 보안을 적용합니다.
    - C. 강력한 ID 및 액세스 제어를 구현합니다.
    - D. 서버리스 아키텍처를 사용합니다.
    - E. 감사 로깅(audit logging)을 활성화합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, D
    </details>

29. 다음 중 Amazon EC2를 사용할 때 고객의 책임에 해당하는 것은 무엇입니까? (두 개 선택)
    - A. 민감한 데이터 보호.
    - B. 기반 인프라의 패치.
    - C. 관리형 데이터베이스의 설정 및 운영.
    - D. 일관된 하드웨어 구성 요소를 유지.
    - E. 서드파티 소프트웨어를 설치하고 구성합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, E
    </details>

30. 왜 어떤 조직은 온프레미스 데이터 센터 대신 AWS를 선택합니까? (두 개 선택)
    - A. 무료 상용 소프트웨어 라이선스.
    - B. 무료 기술 지원.
    - C. 탄력적 리소스(elastic resources).
    - D. 감사를 위한 현장 방문.
    - E. 비용 절감(cost savings).

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C, E
    </details>

31. 다음 중 어떤 AWS 서비스가 보안 분석과 규제 준수 감사(regulatory compliance auditing)를 수행하는 데 도움이 됩니까? (두 개 선택)
    - A. Amazon Inspector.
    - B. AWS Virtual Private Gateway.
    - C. AWS Batch.
    - D. Amazon ECS.
    - E. AWS Config.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, E
    </details>

32. 다음 중 Amazon Elastic Compute Cloud(Amazon EC2)의 NOT(해당되지 않는) 특징은 무엇입니까?
    - A. Amazon EC2는 Serverless Web Service로 간주됩니다.
    - B. Amazon EC2는 처음부터 하드웨어에 투자할 필요를 없앱니다.
    - C. Amazon EC2는 필요에 따라 가상 서버를 얼마든지(많이/적게) 시작할 수 있습니다.
    - D. Amazon EC2는 확장 가능한 컴퓨팅을 제공합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

33. 이벤트로만 트리거되어 실행되는 코드를 처리하는 AWS 컴퓨트 서비스는 무엇입니까?
    - A. AWS Lambda.
    - B. Amazon CloudWatch.
    - C. AWS Transit Gateway.
    - D. Amazon EC2.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

34. AWS와 전통적인 IT 유통업체 모두 고객의 요구를 충족하기 위해 다양한 가상 서버를 제공합니다. AWS에서는 이런 가상 서버를 무엇이라고 부릅니까?
    - A. Amazon EBS Snapshots.
    - B. Amazon VPC.
    - C. AWS Managed Servers.
    - D. Amazon EC2 Instances.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

35. AWS Professional Services가 만든 프레임워크로, 조직이 성공적인 클라우드 도입을 위한 로드맵을 설계하는 데 도움이 되는 것은 무엇입니까?
    - A. AWS Secrets Manager.
    - B. AWS WAF.
    - C. AWS CAF.
    - D. Amazon EFS.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

36. TYMO Cloud Corp은 온프레미스 데이터 센터 전체를 AWS로 마이그레이션하려고 합니다. 이동에 대한 비용 대비 효익 분석(cost-benefit analysis)을 수행하려면 어떤 도구를 사용할 수 있습니까?
    - A. AWS Cost Explorer.
    - B. AWS TCO Calculator.
    - C. AWS Budgets.
    - D. AWS Pricing Calculator.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

37. 다음 중 AWS Well-Architected Framework의 Operational Excellence(운영 우수성) 필러를 지원하는 활동은 무엇입니까?
    - A. AWS Trusted Advisor를 사용해 활용도가 낮은 리소스를 찾습니다.
    - B. AWS CloudTrail을 사용해 사용자 활동을 기록합니다.
    - C. AWS CloudFormation을 사용해 인프라를 코드로 관리합니다.
    - D. 여러 가용 영역에 애플리케이션을 배포합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

38. 많은 스타트업 회사가 전통적인 온프레미스 솔루션보다 AWS를 선호하는 이유는 무엇입니까? (두 개 선택)
    - A. AWS는 비즈니스가 성공하면 나중에 결제할 수 있게 해줍니다.
    - B. AWS는 다른 어떤 클라우드 제공업체보다 더 빠르게 완전한 데이터 센터를 구축할 수 있습니다.
    - C. AWS를 사용하면 데이터 센터를 구축하고 관리하는 데 시간을 쓰는 대신, 비즈니스 활동에 집중해 출시 기간(time-to-market)을 줄일 수 있습니다.
    - D. AWS는 운영 비용(operational expenditure)에 투자할 필요를 없앱니다.
    - E. AWS를 사용하면 큰 규모의 자본 지출(CapEx)을 낮은 변동 비용으로 대체할 수 있습니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C, E
    </details>

39. DynamoDB를 사용했을 때의 이점은 무엇입니까? (두 개 선택)
    - A. 필요한 처리량(throughput) 용량을 충족하도록 자동으로 스케일합니다.
    - B. 현재 수요에 맞춰 조정 가능한(resizable) 인스턴스를 제공합니다.
    - C. 관계형 및 비관계형(relational/non-relational) 데이터 모델을 모두 지원합니다.
    - D. 매우 낮은(단일 자리 밀리초 수준) 레이턴시를 제공합니다.
    - E. CouchDB, MongoDB 같은 가장 인기 있는 NoSQL 데이터베이스 엔진을 지원합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, D
    </details>

40. Amazon S3에서 저장 데이터(at rest)를 보호하기 위해 사용할 수 있는 것은 무엇입니까? (두 개 선택)
    - A. 버전 관리(Versioning).
    - B. 중복 제거(Deduplication).
    - C. 권한(Permissions).
    - D. 암호 해독/복호화(Decryption).
    - E. 변환(Conversion).

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, C
    </details>

41. AWS Migration Acceleration Program(MAP)의 일부로서, 엔터프라이즈가 AWS를 채택(Enterprise adoption)하는 속도를 높이기 위해 AWS는 무엇을 제공합니까? (두 개 선택)
    - A. AWS Partners.
    - B. AWS Artifact.
    - C. AWS Professional Services.
    - D. Amazon Athena.
    - E. Amazon PinPoint.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, C
    </details>

42. AWS는 예상치 못한 요금이 청구서에 발생하는 것을 방지하기 위해 몇 가지 권장 사항을 제시합니다. 다음 중 이런 권장 사항에 해당하지 않는 것은 무엇입니까?
    - A. EC2 인스턴스를 종료(termination)한 후 사용하지 않는 EBS 볼륨을 삭제합니다.
    - B. 사용하지 않는 AutoScaling launch configuration을 삭제합니다.
    - C. 사용하지 않는 Elastic Load Balancer를 삭제합니다.
    - D. EC2 인스턴스를 종료한 후 사용하지 않는 Elastic IP를 해제(releasing)합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

43. 회사가 지난 몇 달 동안의 AWS 지출을 시각화(visualize)할 수 있도록 돕는 AWS 도구는 무엇입니까?
    - A. AWS Cost Explorer.
    - B. AWS Pricing Calculator.
    - C. AWS Budgets.
    - D. AWS Consolidated Billing.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

44. AWS에서 워크로드를 실행할 때 고객이 책임지지 않는 것은 무엇입니까? (두 개 선택)
    - A. 침투 테스트(penetration tests)를 수행합니다.
    - B. 용량을 예약(reserving)합니다.
    - C. 데이터 센터 운영을 수행합니다.
    - D. 감사 및 규제 준수(compliance) 업무를 수행합니다.
    - E. 인프라 보안을 수행합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C, E
    </details>

45. 다음 중 전 세계 200개가 넘는 국가로 프로모션 문자 메시지(SMS)를 보내는 데 사용할 수 있는 AWS 서비스는 무엇입니까?
    - A. Amazon Simple Email Service (Amazon SES).
    - B. Amazon Simple Storage Service (Amazon S3).
    - C. Amazon Simple Notification Service (Amazon SNS).
    - D. Amazon Simple Queue Service (Amazon SQS).

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

46. 다음 중 어떤 것들을 사용하면 새 RDS 인스턴스를 만들 수 있습니까? (두 개 선택)
    - A. AWS CodeDeploy.
    - B. AWS Quick Starts.
    - C. AWS CloudFormation.
    - D. AWS DMS.
    - E. AWS Management Console.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C, E
    </details>

47. AWS를 사용하는 주요 장점 중 하나는 비용 절감입니다. AWS는 Amazon EC2 인스턴스를 실행하는 비용을 줄이기 위해 무엇을 제공합니까?
    - A. 낮은 월 인스턴스 유지보수 비용.
    - B. 저렴한 인스턴스 태깅.
    - C. 초 단위 인스턴스 과금.
    - D. 낮은 인스턴스 시작(시작/런치) 수수료.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

48. 고객이 원하는 비즈니스 결과를 달성하도록 돕는 AWS 그룹은 무엇입니까?
    - A. AWS Security Team.
    - B. AWS Professional Services.
    - C. AWS Trusted Advisor.
    - D. AWS Concierge Support Team.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

49. 고객 데이터를 암호화하는 데 사용되는 키를 관리하는 데 사용되는 AWS 서비스 또는 기능은 무엇입니까?
    - A. AWS KMS.
    - B. AWS Service Control Policies (SCPs).
    - C. Multi-Factor Authentication (MFA).
    - D. Amazon Macie.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

50. 다음 중 고객이 AWS SOC & PCI 보고서를 다운로드할 수 있게 해주는 AWS 서비스는 무엇입니까?
    - A. AWS Well-Architected Tool.
    - B. AWS Artifact.
    - C. AWS Glue.
    - D. Amazon Chime.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

