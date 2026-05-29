# Intent Adapter Table

Maps abstract ButtonIntent / DialogIntent / ToastIntent / SurfaceIntent enums to per-platform native widget choices.

## ButtonIntent → Platform Widget

| Intent | iOS (HIG) | Android (M3) | Web (shadcn) |
|--------|-----------|--------------|--------------|
| Primary | CupertinoButton + systemBlue bg | FilledButton | ShadButton.primary |
| Secondary | CupertinoButton + systemGray bg | OutlinedButton | ShadButton.outline |
| Tertiary | CupertinoButton + clear bg | TextButton | ShadButton.ghost |
| Text | Text with tap gesture | TextButton | ShadButton.link |
| Destructive | CupertinoButton + systemRed | FilledButton + error color | ShadButton.destructive |

## DialogIntent → Platform Widget

| Intent | iOS (HIG) | Android (M3) | Web (shadcn) |
|--------|-----------|--------------|--------------|
| Confirmation | CupertinoAlertDialog | AlertDialog + confirm | ShadAlertDialog |
| Destructive | CupertinoAlertDialog + destructive | AlertDialog + destructive | ShadAlertDialog.destructive |
| Informational | CupertinoAlertDialog | AlertDialog | ShadAlertDialog |

## SurfaceIntent → Platform Widget

| Intent | iOS (HIG) | Android (M3) | Web (shadcn) |
|--------|-----------|--------------|--------------|
| Default | Container + systemBackground | Surface | ShadCard |
| Glass | UiKitView + glassEffect | Material + elevation 1 | liquid-glass CSS |
| Elevated | Container + shadow | Surface + elevation 3 | ShadCard + shadow |
