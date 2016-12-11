libue
=====

Zero dependency minimal library for interacting with Linux hot-plug events.


Installation
------------

Just drop the header file into your C project.


Usage
-----

```C
struct uevent_listener listener;
struct uevent uev;
int re;

re = ue_init_listener(&listener);
if (re < 0) {
    fprintf(stderr, "Failed to initilize libue listener, err: %d\n", re);
    return;
}

/* blocking call */
while ((re = ue_wait_for_event(&listener, &uev)) == 0) {
    switch (uev.action) {
    case UEVENT_ACTION_ADD:
        printf("Device %s added.", uev.devpath);
        break;
    case UEVENT_ACTION_REMOVE:
        printf("Device %s removed.", uev.devpath);
        break;
    }
}
```
