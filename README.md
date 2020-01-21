# ElectronicLeadscrew
Electronic leadscrew config + UI for LinuxCNC

![UI Preview](/ElectronicLeadscrew.JPG)

Simplified network chart:

```
 Machine settings:

 hm2_7i96.0.encoder.00.scale          = Encoder pulses per REVOLUTION 
 hm2_7i96.0.stepgen.00.position-scale = Stepper pulses per MM
 hm2_7i96.0.stepgen.01.position-scale = Stepper pulses per MM

                                        +--------------+
                                        |              |.scale
                                        |   hm2_7i96   |
                                        | 0.encoder.00 |.position
                                        |              |    +
+--------+                              +--------------+    |
|        |                                                  |
|        |                                                  |
|        |.position_a<--------------------------------------+-------------------------+
|        |                                                  |                         |
|        |.offset_x_encoder+-->scale.3.offset               |                         |
|        |                                             +----v----+               +----v----+
|        |.offset_x_stepper+-->scale.5.offset          | scale.0 |.offset        | scale.3 |.offset
|        |                                             +----+----+               +----+----+
|        |.offset_z_encoder+-->scale.0.offset               |                         |
|        |                                                  v                         v
|lathe_ui|.offset_z_stepper+-->scale.2.offset          +----+----+               +----+----+
|        |                                             | scale.1 |.scale         | scale.4 |.scale
|        |.forward_x+--------->scale.1.scale           +----+----+               +----+----+
|        |                                                  |                         |
|        |.forward_z+--------->scale.4.scale                v                         v
|        |                                             +----+----+               +----+----+
|        |                                             | scale.2 |.offset        | scale.5 |.offset
|        |.position_x<--+                              +----+----+               +----+----+
|        |              |                                   |                         |
|        |              |                                   |                         |
|        |.position_z   |                                   +------------+            +---------------------------------------+
+--------+     ^        |                                                |                                                    |
               |  +-----+           +--------------+                     |                 +--------------+                   |
               |  |                 |              |.position-scale      |                 |              |.position-scale    |
               +-------+.position_fb|   hm2_7i96   |                     |     .position_fb|   hm2_7i96   |                   |
                  |                 | 0.stepgen.00 |                     |          +      | 0.stepgen.01 |                   |
                  |                 |              |.position-cmd<-------+          |      |              |.position-cmd<-----+
                  |                 +--------------+                                |      +--------------+
                  |                                                                 |
                  +-----------------------------------------------------------------+
```
