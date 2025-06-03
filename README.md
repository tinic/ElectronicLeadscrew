# ElectronicLeadscrew

> [!NOTE]
> A modernized version of this project is available [here](https://github.com/tinic/el-linuxcnc-electron).

This is a standalone electronic leadscrew HAL configuration + Qt based UI for lathes. It essentially brings back manual control to lathes which have been converted to CNC.

Background: Many hobbyists convert their manual lathe to function as a CNC machine but do not want to lose the ability to use the machine in manual mode. This configuration make this possible. LinuxCNC in this case operates like a gearbox with a few additional features.

Please note that for this to function you have to wire up the enable/disable signal on your stepper drivers, which is usually not required for pure CNC operation.

Debian packages required: python-dbus python-xlib python-pyqt5 python-pyqt5.qsci

![UI Preview](/ElectronicLeadscrew.JPG)

Parts used for this particular example:

- Mesa 7i96 board
- Clone/fake E6B2-CWZ6C Omron encoder (2880 pulses per revolution)
- 2x DM680T stepper drivers (set to 3200 micro steps)
- 2x NEMA23 381oz/in 3.5A Single Shaft Stepper Motor KL23H2100-35-4A
- Mean Well NES-350-36 36V 350 Watt Switching Power Supply 110-240 Volt
- Asus VT168H 15.6” 1366x768 HDMI VGA 10-Point Touch
- ASRock IMB-150N Intel Celeron N2930 Dual LAN industrial Mini-ITX Server Board

Simplified HAL network chart (note that some required signals like enable/disable are not represented here):

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
