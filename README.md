# foxypack-x-twikit

Telegram integration module for **FoxyPack** based on **Twikit**.

Provides link analysis and statistics collection for Twitter accounts and posts.

---

## Basic usage

### Analyze Twitter links

Add a module to the FoxyPack controller for analyzing Twitter links.

```python
from foxypack import FoxyPack
from foxypack_x_twikit import FoxyTwitterAnalysis

parser = FoxyPack().with_foxy_analysis(
    FoxyTwitterAnalysis()
)

parser.get_analysis("https://x.com/elonmusk")
```

### Collect statistics

Add a module to the FoxyPack controller to collect statistics by Twitter links.

```python
from foxy_entities import EntitiesController
from foxypack import FoxyPack
from foxypack_x_twikit import (
    TwitterAccount,
    FoxyTwitterStat,
)

account = TwitterAccount(
    username="your_username",
    email="your_mail",
    password="your_password",
    cookies_file="path_to_your_cookies.json",
)

controller = EntitiesController()
controller.add_entity(account)

parser = FoxyPack().with_foxy_stat(
    FoxyTwitterStat(entities_controller=controller)
)

parser.get_statistics("https://x.com/elonmusk/status/2000078735622721927")
```

### Supported links

* Public accounts
* Public posts

### Supported content types

* account
* post
