# Motion Adapter Table

Maps MotionIntent enums to per-platform timing curves.

| MotionIntent | iOS (HIG) | Android (M3) | Web |
|--------------|-----------|--------------|-----|
| Press | spring(0.3, 0.6) scale 0.97 | 100ms easeOut scale 0.95 | 100ms ease-out |
| Select | 200ms easeInOut | 200ms easeInOut | 200ms ease-in-out |
| Toggle | 150ms easeOut | 150ms easeOut | 150ms ease-out |
| Expand | 300ms easeOut | 300ms easeOut | 300ms ease-out |
| Collapse | 250ms easeIn | 250ms easeIn | 250ms ease-in |
| Present | 400ms spring(0.4, 0.7) | 300ms easeOut | 300ms ease-out |
| Dismiss | 300ms easeIn | 250ms easeIn | 250ms ease-in |
| ToastEnter | N/A (use dialog) | 300ms easeOut slide up | 300ms ease-out |
| ToastExit | N/A (use dialog) | 250ms easeIn fade | 250ms ease-in |
| NavPush | 350ms easeOut slide left | 300ms easeOut slide left | 300ms ease-out |
| NavPop | 300ms easeIn slide right | 250ms easeIn slide right | 250ms ease-in |
| Focus | 200ms easeOut | 200ms easeOut | 200ms ease-out |
| LoadingPulse | 1.5s easeInOut repeat | 1.5s easeInOut repeat | 1.5s ease-in-out infinite |
| ErrorShake | 500ms keyframe (3 shakes) | 500ms keyframe (3 shakes) | 500ms shake keyframe |
| SuccessCheck | 300ms easeOut scale 1.1 | 300ms easeOut scale 1.1 | 300ms ease-out |
