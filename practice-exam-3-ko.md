---
layout: exam
---

# 연습 시험 3

1. AWS에서는 파일을 어디에 저장할 수 있습니까? (두 개 선택)
    - A. Amazon EFS.
    - B. Amazon SNS.
    - C. Amazon EBS.
    - D. Amazon ECS.
    - E. Amazon EMR.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, C
    </details>

2. 다음 중 AWS 서비스 중에서 분산 시스템에서 메시지를 저장하고 신뢰성 있게 전달하는 데 사용할 수 있는 것은 무엇입니까?
    - A. Amazon Simple Queue Service.
    - B. AWS Storage Gateway.
    - C. Amazon Simple Email Service.
    - D. Amazon Simple Storage Service.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

3. 다음 중, 고객이 Amazon EC2를 1년 또는 3년 기간으로 약정(commit)하여 총 컴퓨팅 비용을 줄일 수 있게 해주는 AWS의 결제 모델을 설명하는 것은 무엇입니까?
    - A. AWS가 성장할수록 더 적게 결제합니다.
    - B. 사용한 만큼 결제합니다.
    - C. 더 많이 사용하면 더 적게 결제합니다.
    - D. 예약하면 절약할 수 있습니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

4. 한 회사가 온프레미스 DB를 Amazon RDS로 마이그레이션하고 있습니다. Amazon RDS 비용을 최소화하려면 회사는 무엇을 해야 합니까?
    - A. 마이그레이션 전후로 적절한 크기(Right-size)를 조정합니다.
    - B. 멀티 리전 Active-Passive 아키텍처를 사용합니다.
    - C. 온디맨드 용량 예약(On-demand Capacity Reservations)과 세이빙 플랜(Saving Plans)을 함께 사용합니다.
    - D. 멀티 리전 Active-Active 아키텍처를 사용합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

5. Amazon RDS 데이터베이스 인스턴스에서 사용하는 기본 스토리지 서비스는 무엇입니까?
    - A. Amazon Glacier.
    - B. Amazon EBS.
    - C. Amazon EFS.
    - D. Amazon S3.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

6. 한 회사가 마이크로서비스 프레임워크로 새 애플리케이션을 개발하고 있습니다. 애플리케이션의 성능과 레이턴시 문제가 발생했습니다. 이 문제를 해결(troubleshoot)하는 데 사용해야 하는 AWS 서비스는 무엇입니까?
    - A. AWS CodePipeline.
    - B. AWS X-Ray.
    - C. Amazon Inspector.
    - D. AWS CloudTrail.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

7. 다음 중 네이티브 멀티-AZ 내결함성을 염두에 두고 설계된 AWS 서비스는 무엇입니까? (두 개 선택)
    - A. Amazon Redshift.
    - B. AWS Snowball.
    - C. Amazon Simple Storage Service.
    - D. Amazon EBS.
    - E. Amazon DynamoDB.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C, E
    </details>

8. Amazon RDS에서 데이터베이스 가용성을 높이기 위해 사용할 수 있는 기능은 무엇입니까? (두 개 선택)
    - A. AWS Regions.
    - B. Multi-AZ 배포(Multi-AZ Deployment).
    - C. 자동 패치(Automatic patching).
    - D. Read Replicas.
    - E. Edge Locations.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B, D
    </details>

9. Sarah는 Northern California(us-west-1) 리전에 애플리케이션을 배포했습니다. 애플리케이션 트래픽을 확인해 보니 약 30%가 아시아에서 들어오고 있습니다. 아시아 사용자들의 레이턴시를 줄이려면 무엇을 할 수 있습니까?
    - A. 동일 리전 내 여러 가용 영역(Availability Zones)으로 현재 리소스를 복제합니다.
    - B. 아시아의 호스팅 제공업체로 애플리케이션을 마이그레이션합니다.
    - C. 웹사이트 콘텐츠를 다시 생성합니다.
    - D. CloudFront를 사용해 CDN을 만들고, 아시아에 가깝고 아시아 내 Edge Locations에 콘텐츠를 캐시하도록 합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

10. 한 조직은 많은 시스템을 운영하고 다양한 AWS 제품을 사용합니다. 다음 중 각 개발자가 이러한 제품과 상호작용하는 방식을 제어할 수 있게 해주는 서비스는 무엇입니까?
    - A. AWS Identity and Access Management.
    - B. Amazon RDS.
    - C. Network Access Control Lists.
    - D. Amazon EMR.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

11. Amazon EC2를 사용하는 것은 다음 중 어떤 클라우드 컴퓨팅 모델에 해당합니까?
    - A. Iaas & SaaS.
    - B. IaaS.
    - C. SaaS.
    - D. PaaS.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

12. AWS에서 애플리케이션을 만들 때의 모범 사례로 옳은 것은 무엇입니까?
    - A. 최소 권한의 원칙을 적용하여 물리적 보안을 강화합니다.
    - B. 신뢰할 수 있는 벤더의 하드웨어에서 애플리케이션이 실행되도록 합니다.
    - C. 성능을 유지하기 위해 IAM 정책을 사용합니다.
    - D. 애플리케이션 구성 요소를 디커플링(decouple)하여 서로 독립적으로 실행되게 합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

13. 회사가 사진과 비디오를 저장하고 검색하는 새 애플리케이션을 설계하고 있습니다. 다음 중 기반 스토리지 메커니즘으로 추천해야 하는 서비스는 무엇입니까?
    - A. Amazon EBS.
    - B. Amazon SQS.
    - C. Amazon Instance store.
    - D. Amazon S3.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

14. Amazon Glacier는 Amazon S3의 스토리지 클래스이며, [...] & [...] 를 저장하는 데 적합합니다. (두 개 선택)
    - A. Active archives.
    - B. Dynamic websites’ assets.
    - C. 장기 분석 데이터(Long-term analytic data).
    - D. Active databases.
    - E. Cached data.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, C
    </details>

15. Amazon Elastic Beanstalk는 무엇을 제공합니까?
    - A. 애플리케이션 배포를 자동화하는 PaaS 솔루션.
    - B. Amazon ECS를 위한 컴퓨트 엔진(compute engine).
    - C. AWS 및 온프레미스 서버와 함께 사용할 수 있는 확장 가능한 파일 스토리지 솔루션.
    - D. NoSQL 데이터베이스 서비스.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

16. Amazon EC2 인스턴스를 대상으로, 취약점(vulnerabilities)을 확인하기 위해 자동화된 네트워크 평가를 수행하는 AWS 서비스는 무엇입니까?
    - A. Amazon Kinesis.
    - B. 보안 그룹(Security groups).
    - C. Amazon Inspector.
    - D. AWS Network Access Control Lists.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

17. Shared Responsibility Model에서 고객이 AWS로부터 완전히 상속(inherit)받는 컨트롤은 무엇입니까? (두 개 선택)
    - A. 패치 관리(Patch management controls).
    - B. 데이터베이스 컨트롤(Database controls).
    - C. 인지 및 교육(Awareness & Training).
    - D. 환경 컨트롤(Environmental controls).
    - E. 물리적 컨트롤(Physical controls).

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D, E
    </details>

18. 한 회사는 Amazon RDS에서 최소 3년 동안 데이터베이스를 호스팅해야 합니다. 다음 중 가장 비용 효율적인 옵션은 무엇입니까?
    - A. 예약 인스턴스 - 선결제 없음(Reserved instances - No Upfront).
    - B. 예약 인스턴스 - 부분 선결제(Reserved instances - Partial Upfront).
    - C. 온디맨드 인스턴스(On-Demand instances).
    - D. 스팟 인스턴스(Spot Instances).

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

19. 애플리케이션이 최근 큰 폭으로 전 세계적으로 성장했으며, 국제 사용자들이 높은 레이턴시를 불평하고 있습니다. 국제 사용자들의 경험을 개선하는 데 도움이 되는 AWS 특성은 무엇입니까?
    - A. 탄력성(Elasticity).
    - B. 글로벌 범위(Global reach).
    - C. 데이터 내구성(Data durability).
    - D. 고가용성(High availability).

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

20. Savings Plans는 다음 중 어떤 AWS 컴퓨트 서비스에 대해 제공됩니까? (두 개 선택)
    - A. AWS Batch.
    - B. AWS Outposts.
    - C. Amazon Lightsail.
    - D. Amazon EC2.
    - E. AWS Lambda.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D, E
    </details>

21. 한 회사는 AWS에서 비즈니스 핵심 워크로드를 운영하며, 어떤 다운타임도 허용하지 않습니다. 예기치 않은 자연재해 상황에서 워크로드를 보호하기 위해 다음 중 권장 모범 사례는 무엇입니까?
    - A. 전 세계 여러 Edge Locations에 데이터를 복제하고, Amazon CloudFront를 사용해 장애(outage) 발생 시 자동 페일오버를 수행합니다.
    - B. 동일 AWS 리전 내 여러 가용 영역(Availability Zones)에 걸쳐 AWS 리소스를 배포합니다.
    - C. 다른 서브넷에 시점 기준 백업(point-in-time backups)을 생성하고, 재해가 발생하면 그 데이터를 복구합니다.
    - D. 다른 AWS 리전으로 AWS 리소스를 배포하고, Active-Active 재해 복구 전략을 구현합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

22. AWS 서비스 한도(service limits)에 대해 다음 중 올바른 설명은 무엇입니까? (두 개 선택)
    - A. 서비스 한도를 늘리기 위해 AWS 지원에 문의할 수 있습니다.
    - B. 모든 IAM 사용자는 동일한 서비스 한도를 갖습니다.
    - C. AWS에는 서비스 한도가 없습니다.
    - D. AWS Trusted Advisor를 사용해 서비스 한도를 모니터링할 수 있습니다.
    - E. Amazon Simple Email Service는 사용량이 서비스 한도에 접근할 때 이메일 알림을 보내는 책임을 집니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, D
    </details>

23. 모든 AWS 서비스와 리소스를 관리하기 위해 스크립트를 사용할 수 있게 해주는 AWS 도구는 무엇입니까?
    - A. AWS Console.
    - B. AWS Service Catalog.
    - C. AWS OpsWorks.
    - D. AWS CLI.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

24. 하이브리드 클라우드 아키텍처를 구축할 때 사용할 수 있는 연결 옵션은 무엇입니까? (두 개 선택)
    - A. AWS Artifact.
    - B. AWS Cloud9.
    - C. AWS Direct Connect.
    - D. AWS CloudTrail.
    - E. AWS VPN.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C, E
    </details>

25. 한 회사가 여러 Amazon EC2 인스턴스에 새로운 웹 애플리케이션을 배포했습니다. 들어오는 HTTP 트래픽이 인스턴스에 고르게 분산되도록 하려면 아래 중 무엇을 사용해야 합니까?
    - A. AWS EC2 Auto Recovery.
    - B. AWS Auto Scaling.
    - C. AWS Network Load Balancer.
    - D. AWS Application Load Balancer.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

26. 다음 중, MySQL과 호환되는 관계형 데이터베이스 서비스이면서 수요에 따라 컴퓨트 용량을 자동으로 확장하는 AWS 제공 항목은 무엇입니까?
    - A. Amazon Neptune.
    - B. Amazon Aurora.
    - C. Amazon RDS for SQL Server.
    - D. Amazon RDS for PostgreSQL.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

27. 다음 중 EC2 인스턴스를 DDoS 공격으로부터 보호하는 데 도움이 되는 것은 무엇입니까? (두 개 선택)
    - A. AWS CloudHSM.
    - B. Security Groups.
    - C. AWS Batch.
    - D. AWS IAM.
    - E. Network Access Control Lists(Network ACLs).

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B, E
    </details>

28. 많은 양의 데이터 세트에서 높은 수준의 쿼리 성능을 지원하는 AWS 데이터 웨어하우스 서비스는 무엇입니까?
    - A. Amazon Redshift.
    - B. Amazon Kinesis.
    - C. Amazon DynamoDB.
    - D. Amazon RDS.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

29. AWS에서 애플리케이션을 실행하는 비용과 온프레미스에서 실행하는 비용을 비교하기 위한 TCO 분석을 수행할 때 고려해야 하는 것은 무엇입니까?
    - A. 애플리케이션 개발.
    - B. 시장 조사.
    - C. 비즈니스 분석.
    - D. 물리 하드웨어.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

30. Linux 기반 Amazon EC2 사용에 대해 AWS는 어떻게 청구합니까?
    - A. EC2 인스턴스는 1초 단위로 과금되며, 최소 1분이 부과됩니다.
    - B. EC2 인스턴스는 1시간 단위로 과금되며, 최소 1일이 부과됩니다.
    - C. EC2 인스턴스는 1분 단위로 과금되며, 최소 1시간이 부과됩니다.
    - D. EC2 인스턴스는 1일 단위로 과금되며, 최소 1개월이 부과됩니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

31. 다음 중 EC2 인스턴스에 지불하는 가격에 영향을 주는 것은 무엇입니까? (두 개 선택)
    - A. 인스턴스 타입(Instance type).
    - B. 인스턴스를 프로비저닝하는 가용 영역(Availability Zone).
    - C. 로드 밸런싱(Load balancing).
    - D. 버킷 수(Number of buckets).
    - E. 프라이빗 IP 수(Number of private IPs).

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, B
    </details>

32. 한 고객이 새로 배포된 Amazon EC2 인스턴스를 구성하는 데 많은 시간을 썼습니다. 이후 워크로드가 증가하자 고객은 동일한 구성으로 EC2 인스턴스를 하나 더 프로비저닝하기로 결정합니다. 고객은 어떻게 이 작업을 수행할 수 있습니까?
    - A. 기존 인스턴스로부터 AWS Config 템플릿을 생성하고, 그 템플릿으로 새 인스턴스를 시작(런치)합니다.
    - B. 기존 인스턴스로부터 EBS 스냅샷을 생성합니다.
    - C. EC2에 Aurora를 설치한 뒤, 거기서부터 새 인스턴스를 시작합니다.
    - D. 기존 인스턴스로부터 AMI를 생성한 후, 그 AMI로 새 인스턴스를 시작합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

33. 한 회사는 AWS Organizations를 사용해 모든 AWS 계정을 관리합니다. 다음 중 회사가 각 개별 계정에서 허용되는 서비스와 작업을 제한할 수 있게 해주는 것은 무엇입니까?
    - A. IAM Principals.
    - B. AWS Service Control Policies (SCPs).
    - C. IAM policies.
    - D. AWS Fargate.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

34. 다음 중 AWS 클라우드의 민첩성(agility)을 설명하는 것은 무엇입니까?
    - A. AWS를 통해 전 세계 여러 리전에 애플리케이션을 호스팅할 수 있습니다.
    - B. AWS는 가능한 한 낮은 비용으로 커스터마이즈 가능한 하드웨어를 제공합니다.
    - C. AWS는 몇 분 만에 리소스를 프로비저닝할 수 있게 해줍니다.
    - D. AWS는 비용을 줄이기 위해 선결제로 지불할 수 있게 해줍니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: C
    </details>

35. Amazon Relational Database Service(RDS)를 사용하는 이점은 무엇입니까? (두 개 선택)
    - A. 낮은 관리 부담.
    - B. 기반 호스트에 대한 완전한 제어.
    - C. 조정 가능한 컴퓨트 용량(resizable compute capacity).
    - D. 더 크거나 더 작은 인스턴스 타입으로 자동 확장합니다.
    - E. 문서 및 키-값 데이터 구조(document and key-value data structure)를 지원합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, C
    </details>

36. 온프레미스 네트워크와 AWS 클라우드 사이에, 인터넷 프로토콜 보안(Internet Protocol Security, IPSec)을 사용해 암호화된 연결을 설정하는 연결 옵션은 무엇입니까?
    - A. Internet Gateway.
    - B. AWS IQ.
    - C. AWS Direct Connect.
    - D. AWS Site-to-Site VPN.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

37. 전화와 채팅을 통해 기술 지원 엔지니어에 24x7로 접근할 수 있게 해주는 AWS 지원의 최소 수준은 무엇입니까?
    - A. Enterprise Support.
    - B. Developer Support.
    - C. Basic Support.
    - D. Business Support.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

38. 다음 중 AWS에서 네트워크 트래픽을 제어하는 데 사용되는 것은 무엇입니까? (두 개 선택)
    - A. Network Access Control Lists (NACLs).
    - B. Key Pairs.
    - C. Access Keys.
    - D. IAM Policies.
    - E. Security Groups.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, E
    </details>

39. 한 회사가 AWS에서 미디어 트랜스코딩 애플리케이션을 개발했습니다. 이 애플리케이션은 하드웨어 장애로부터 빠르게 복구하도록 설계되어 있습니다. 다음 중 어떤 인스턴스 타입이 가장 비용 효율적인 선택입니까?
    - A. 예약 인스턴스(Reserved instances).
    - B. 스팟 인스턴스(Spot Instances).
    - C. 온디맨드 인스턴스(On-Demand instances).
    - D. 전용 인스턴스(Dedicated instances).

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

40. 다음 중 AWS 모든 리전에서 모든 AWS 서비스의 현재 상태를 제공하는 AWS 서비스는 무엇입니까?
    - A. AWS Service Health Dashboard.
    - B. AWS Management Console.
    - C. Amazon CloudWatch.
    - D. AWS Personal Health Dashboard.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

41. 다음 중 어떤 AWS 서비스 또는 기능을 사용하면 서로 다른 프로그래밍 언어에서 AWS 서비스를 호출할 수 있습니까?
    - A. AWS Software Development Kit.
    - B. AWS Command Line Interface.
    - C. AWS CodeDeploy.
    - D. AWS Management Console.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

42. 다음 중 어떤 AWS 서비스가 새 도메인 이름을 등록하는 데 사용할 수 있습니까?
    - A. Amazon Personalize.
    - B. Amazon Route 53.
    - C. AWS KMS.
    - D. AWS Config.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

43. 앱 개발 회사들은 출시 기간을 줄이고 고객 만족도를 높이기 위해 AWS로 사업을 옮깁니다. 애플리케이션을 더 빠르게 배포하도록 돕는 AWS 자동화 도구는 무엇입니까? (두 개 선택)
    - A. AWS CloudFormation.
    - B. AWS Migration Hub.
    - C. AWS IAM.
    - D. AWS Elastic Beanstalk.
    - E. Amazon Macie.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A, D
    </details>

44. 다음 중 비용 최적화(cost-optimization) 권장 사항을 제공하는 AWS 서비스는 무엇입니까?
    - A. AWS Trusted Advisor.
    - B. AWS Pricing Calculator.
    - C. Amazon QuickSight.
    - D. AWS X-Ray.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

45. 한 회사는 전 세계 여러 AWS 리전에 수백 개의 VPC를 보유하고 있습니다. VPC들 간 연결 관리(connection management)를 단순화하기 위해 AWS가 제공하는 서비스는 무엇입니까?
    - A. VPC Peering.
    - B. AWS Transit Gateway.
    - C. Amazon Connect.
    - D. Security Groups.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

46. 예약된 EC2 인스턴스를 구매할 때의 이점 1개와 단점 1개는 무엇입니까? (두 개 선택)
    - A. 인스턴스는 AWS가 어떤 때든 알림 없이 종료할 수 있습니다.
    - B. 예약 인스턴스는 최소 1년의 가격 약정이 필요합니다.
    - C. 전용 인스턴스를 사용하는 경우 추가 요금이 없습니다.
    - D. 예약 인스턴스는 온디맨드 인스턴스 대비 유의미한 할인을 제공합니다.
    - E. 예약 인스턴스는 주기적인(간헐적) 워크로드에 가장 적합합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B, D
    </details>

47. 모든 AWS 리전에는 여러 가용 영역(Availability Zones)이 포함되어 있는 이유는 무엇입니까?
    - A. 여러 가용 영역을 사용하면 더 탄력적이고 고가용 아키텍처를 만들 수 있습니다.
    - B. 여러 가용 영역을 사용하면 단일 가용 영역에 배포하는 것보다 전체 비용이 낮아집니다.
    - C. 여러 가용 영역을 사용하면 데이터 복제 및 글로벌 확장이 가능합니다.
    - D. 한 리전 내 여러 가용 영역은 해당 리전에서 사용할 수 있는 스토리지 용량을 증가시킵니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

48. 다음 중, 항상 가용해야 하는 기간이 2개월인 EC2 인스턴스 집합을 실행할 때 가장 비용 효율적인 구매 옵션은 무엇입니까?
    - A. 온디맨드 인스턴스(On-Demand Instances).
    - B. 스팟 인스턴스(Spot Instances).
    - C. 예약 인스턴스(Reserved Instances) - 전액 선결제(All Upfront).
    - D. 예약 인스턴스(Reserved Instances) - 선결제 없음(No Upfront).

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: A
    </details>

49. 다음 중 여러 가용 영역에서 애플리케이션을 실행하는 이점은 무엇입니까?
    - A. AWS 서비스 한도를 초과할 수 있습니다.
    - B. 서버와 전 세계 사용자 사이의 애플리케이션 응답 시간을 줄입니다.
    - C. 사용 가능한 컴퓨트 용량을 늘립니다.
    - D. 애플리케이션의 가용성을 높입니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: D
    </details>

50. 데이터 보안은 AWS의 최우선 과제 중 하나입니다. AWS는 유용 수명이 끝난 오래된 스토리지 장치를 어떻게 처리합니까?
    - A. AWS는 오래된 장치를 다른 호스팅 제공업체에 판매합니다.
    - B. AWS는 업계 표준 관행에 따라 오래된 장치를 파기(destroy)합니다.
    - C. AWS는 오래된 장치를 재제조(remanufacturing)하기 위해 보냅니다.
    - D. AWS는 오래된 장치를 안전한 곳에 보관합니다.

    <details markdown=1><summary markdown='span'>Answer</summary>
      Correct answer: B
    </details>

