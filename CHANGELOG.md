# CHANGELOG

## v0.4.1 (2024-06-20)

### Chore

* chore: fix release command ([`763fcf3`](https://github.com/KiraLT/certbot-lambda/commit/763fcf3d8ad38b3da3bd35e1294d6444e3c8e2c9))

* chore: publish command fix ([`47ddf71`](https://github.com/KiraLT/certbot-lambda/commit/47ddf71c52dd9bffd2ba3730cf086acd1d08f1ea))

* chore: update semantic_release config ([`632c665`](https://github.com/KiraLT/certbot-lambda/commit/632c665118a312cdf2284ca3aef1a35187024766))

* chore: update dependencies ([`d57b23a`](https://github.com/KiraLT/certbot-lambda/commit/d57b23af5765d2204e947ce3edb68a4bcf149921))

* chore: update GitHub Actions to use latest versions ([`4a218f3`](https://github.com/KiraLT/certbot-lambda/commit/4a218f381b2fb98169afd6429607eca3bdb13cb5))

* chore: dependencies update ([`40d9741`](https://github.com/KiraLT/certbot-lambda/commit/40d974195a81b4ccc7f0f35338e85037fc756fc9))

### Fix

* fix: update to Python 3.11, use complete-platform JSON

The latest supported AWS Lambda runtime is Python 3.11, so upgrade
from Python 3.9 to Python 3.11. To avoid falling into
KiraLT/certbot-lambda#166, specify a complete-platform.json file,
generated using `pex3 interpreter inspect --markers --tags` in an AWS
Lambda Python 3.11 runtime.

Fixes KiraLT/certbot-lambda#166 ([`20c8d92`](https://github.com/KiraLT/certbot-lambda/commit/20c8d920d0c11d5397054d8ab7451b2f71438610))

### Unknown

* Delete .github/workflows/codeql-analysis.yml ([`96c6bc2`](https://github.com/KiraLT/certbot-lambda/commit/96c6bc2806da73b5d2d3e28b2369ce456d822712))

* Delete .github/dependabot.yml ([`6244cb4`](https://github.com/KiraLT/certbot-lambda/commit/6244cb4961e3d7e70a85a94c548b2194c586657f))

* Update devcontainer.json ([`24397ba`](https://github.com/KiraLT/certbot-lambda/commit/24397ba669e6930841fe6cdfc5af47c1e9394132))

## v0.4.0 (2022-12-28)

### Feature

* feat: remove secrets listing to reduce required AWS permissions

closes #107 ([`b16cc62`](https://github.com/KiraLT/certbot-lambda/commit/b16cc6250ca6029ad7e20606441b4a3aef2902cb))

### Unknown

* Merge branch &#39;main&#39; of https://github.com/KiraLT/certbot-lambda ([`1a5963f`](https://github.com/KiraLT/certbot-lambda/commit/1a5963ff2551e45b16cb5946ff75ff1571ca6c06))

## v0.3.0 (2022-12-28)

### Chore

* chore: testmode fix ([`7441c5f`](https://github.com/KiraLT/certbot-lambda/commit/7441c5f435dc424680681495f0f1020ffe0991fa))

* chore: build test fix ([`1ba2794`](https://github.com/KiraLT/certbot-lambda/commit/1ba2794bab3adae51a078b7b15fce28562e68a14))

* chore: ci depts update ([`3138450`](https://github.com/KiraLT/certbot-lambda/commit/313845096f036718a40db946f5faf0d92a157507))

### Feature

* feat: dependencies update ([`56c67e5`](https://github.com/KiraLT/certbot-lambda/commit/56c67e554aa86de8eaafe285b363feb995ff797f))

### Unknown

* Create SECURITY.md ([`32f1e2a`](https://github.com/KiraLT/certbot-lambda/commit/32f1e2ae165d7814ca2b76b91952b4079d20c16d))

* Create devcontainer.json ([`5f5b795`](https://github.com/KiraLT/certbot-lambda/commit/5f5b79577b81ee595cd430aafcd761f9291903d4))

## v0.2.4 (2022-07-30)

### Fix

* fix: credentials file fix ([`2e563f1`](https://github.com/KiraLT/certbot-lambda/commit/2e563f1133d54cd750b104a586b995793454c3b2))

### Unknown

* Merge branch &#39;main&#39; of https://github.com/KiraLT/certbot-lambda ([`a7c1620`](https://github.com/KiraLT/certbot-lambda/commit/a7c1620751c3b9a537db788f78090672572c70e8))

## v0.2.3 (2022-07-30)

### Chore

* chore(deps): bump boto3 from 1.24.40 to 1.24.41

Bumps [boto3](https://github.com/boto/boto3) from 1.24.40 to 1.24.41.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.24.40...1.24.41)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`950599e`](https://github.com/KiraLT/certbot-lambda/commit/950599e9dbf06c65daf0ae055dc975faa4977a9d))

* chore: ci fix ([`71434f2`](https://github.com/KiraLT/certbot-lambda/commit/71434f2006ce461114cb01996cf680389c1aed05))

* chore: ci coverage fix ([`743306d`](https://github.com/KiraLT/certbot-lambda/commit/743306df3c3dab7f7582d4dd51f3f928b36a9458))

### Documentation

* docs: README update ([`a7e318a`](https://github.com/KiraLT/certbot-lambda/commit/a7e318adffb37134155fe60a693b1c1c512d2242))

### Fix

* fix: fix dependency issue, add google cloud function support ([`01630d0`](https://github.com/KiraLT/certbot-lambda/commit/01630d010296729fed0b7d4431f547bd426a852f))

### Test

* test: fix coverage reports ([`99f2f0e`](https://github.com/KiraLT/certbot-lambda/commit/99f2f0e07ce70ecbd3dda0045fbbb10e27eb70c3))

* test: more tests ([`f31a483`](https://github.com/KiraLT/certbot-lambda/commit/f31a4833f4d9c025b125a8c6ba61be382884a372))

* test: added tests ([`509f936`](https://github.com/KiraLT/certbot-lambda/commit/509f936e0ca1006a22430a4564256765f3cb9c7b))

### Unknown

* Merge pull request #7 from KiraLT/dependabot/pip/boto3-1.24.41

chore(deps): bump boto3 from 1.24.40 to 1.24.41 ([`0bdb5f5`](https://github.com/KiraLT/certbot-lambda/commit/0bdb5f5cb5c026d411fb05c01b3e35c8157926f7))

## v0.2.2 (2022-07-29)

### Chore

* chore: ci fix ([`71e8f33`](https://github.com/KiraLT/certbot-lambda/commit/71e8f33825f7a5518e93ced3dac04d27000a4694))

* chore: release ci fix ([`a2e3ae9`](https://github.com/KiraLT/certbot-lambda/commit/a2e3ae9494be10685570ef285ce29395947f8637))

### Ci

* ci: remove poetry cache ([`d22cf8e`](https://github.com/KiraLT/certbot-lambda/commit/d22cf8e75ba757403c0b559362f6a1572f3d0c1a))

### Fix

* fix: release ci ([`331a18f`](https://github.com/KiraLT/certbot-lambda/commit/331a18f9cc189f5a236984aa47a7becdafc6b550))

## v0.2.1 (2022-07-29)

### Chore

* chore: release ci fix ([`3908fde`](https://github.com/KiraLT/certbot-lambda/commit/3908fdeb29f10dae3e199428a1cd479bb5968089))

* chore: release fix ([`4d9530b`](https://github.com/KiraLT/certbot-lambda/commit/4d9530b638681358aed4e0a6542303cccdb8a5a6))

* chore: ci fix ([`79f9920`](https://github.com/KiraLT/certbot-lambda/commit/79f9920418d211da6f3070b545de075bdb6a8898))

* chore: fix release ci ([`e0ec429`](https://github.com/KiraLT/certbot-lambda/commit/e0ec4294aa0e3d1e8a9027f9690cdfd65eb1f63a))

* chore: ci update ([`1f22f8d`](https://github.com/KiraLT/certbot-lambda/commit/1f22f8dd2693e762bcb95b7d2615b9bbb214e802))

### Fix

* fix: dependencies update and settings fix ([`0264d8f`](https://github.com/KiraLT/certbot-lambda/commit/0264d8f1c446b17ed47cf0460a29afca23ca3639))

## v0.2.0 (2022-07-23)

### Chore

* chore: CodeQL workflow ([`3bec9e3`](https://github.com/KiraLT/certbot-lambda/commit/3bec9e3575a67345849778f55227836591c5eee7))

### Feature

* feat: credentials file, propagation seconds and custom certbot args support

Add ability to specify credentials, propagation seconds and custom certbot args by passing environment variables.

closes #1 ([`8ba38bd`](https://github.com/KiraLT/certbot-lambda/commit/8ba38bdc24d87722cd9fb308215d3ed582e85af4))

## v0.1.2 (2022-01-19)

### Documentation

* docs: update CONTRIBUTING.md ([`758ef7d`](https://github.com/KiraLT/certbot-lambda/commit/758ef7d83e87f19b207bfa24dad4f48f11043839))

### Feature

* feat: certbot ability to specify preferred chain to remove expired DST Root CA X3 cert ([`9ddab81`](https://github.com/KiraLT/certbot-lambda/commit/9ddab8141bfa07302cfe630365838661492d19f0))

### Fix

* fix: code improvements ([`4777178`](https://github.com/KiraLT/certbot-lambda/commit/4777178eb2e1c78aaaebffbae0985d15272b7464))

### Unknown

* Merge branch &#39;main&#39; of github.com:KiraLT/certbot-lambda ([`ccc7b7e`](https://github.com/KiraLT/certbot-lambda/commit/ccc7b7e82081375172518fe61395de2d3c73f5ec))

## v0.1.1 (2022-01-18)

### Fix

* fix: support asterisk and multiple domains ([`9e299e7`](https://github.com/KiraLT/certbot-lambda/commit/9e299e7bccf64ee7b3a097b75945a04ce00d8da9))

## v0.1.0 (2022-01-18)

### Breaking

* feat: first release

BREAKING CHANGE: first release ([`569ca9a`](https://github.com/KiraLT/certbot-lambda/commit/569ca9a2c722305bea0da7432f0168f64d447ec2))

### Chore

* chore: build fix ([`df83af6`](https://github.com/KiraLT/certbot-lambda/commit/df83af6c723bffcecbe8f58490a81df269ffac02))

* chore: release fix ([`70d6488`](https://github.com/KiraLT/certbot-lambda/commit/70d6488e2ab6a4eb50f529b9ecb950cb8ef78e8c))

### Documentation

* docs: README update ([`ca5be56`](https://github.com/KiraLT/certbot-lambda/commit/ca5be5673932d636f5bfc8bd0426e439c7c7a551))

* docs: README update ([`124be95`](https://github.com/KiraLT/certbot-lambda/commit/124be95688e7d8c58c82bb178702cb02ea563532))

### Feature

* feat: ability to change AWS secret description ([`963a47c`](https://github.com/KiraLT/certbot-lambda/commit/963a47cc76bf182e26ce7d3094f6f903d4778791))

* feat: auto-release and certs validation ([`bf63ae4`](https://github.com/KiraLT/certbot-lambda/commit/bf63ae493604ad5da656e215c6432687c550512c))

### Unknown

* Update README.md ([`e85caf8`](https://github.com/KiraLT/certbot-lambda/commit/e85caf864d36faed7a2e00db53a3536ccbcbad3a))

* Improvements ([`49305f0`](https://github.com/KiraLT/certbot-lambda/commit/49305f037c0143b938535f4d5c5bec751a611a48))

* base logic ([`3258ca0`](https://github.com/KiraLT/certbot-lambda/commit/3258ca0c2fa5c2bdae0340ca868370ee488f6370))

* Initial commit ([`eaf54ed`](https://github.com/KiraLT/certbot-lambda/commit/eaf54ed1f0f415b93417ef33c76339ec7587d5dd))
