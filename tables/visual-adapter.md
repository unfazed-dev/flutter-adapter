# Visual Adapter Table

Maps abstract design tokens to per-platform concrete values.

## Spacing tokens

| Token | iOS (HIG) | Android (M3) | Web |
|-------|-----------|--------------|-----|
| space.xs | 4pt | 4dp | 0.25rem |
| space.sm | 8pt | 8dp | 0.5rem |
| space.md | 16pt | 16dp | 1rem |
| space.lg | 24pt | 24dp | 1.5rem |
| space.xl | 32pt | 32dp | 2rem |
| space.card | 16pt | 20dp | 1.25rem |
| space.card-gap | 12pt | 16dp | 1rem |

## Radius tokens

| Token | iOS (HIG) | Android (M3) | Web |
|-------|-----------|--------------|-----|
| radius.sm | 6pt | 8dp (shape.small) | 0.375rem |
| radius.md | 10pt | 12dp (shape.medium) | 0.5rem |
| radius.lg | 14pt | 16dp (shape.large) | 0.75rem |
| radius.card | 14pt | 12dp | 0.75rem |

## Color semantics (light mode)

| Token | iOS (HIG) | Android (M3) | Web |
|-------|-----------|--------------|-----|
| bg | systemBackground (#F2F2F7) | surface (#FFFBFE) | hsl(var(--background)) |
| surface | secondarySystemBackground (#FFFFFF) | surface-container-low (#F3EDF7) | hsl(var(--card)) |
| primary | systemBlue (#007AFF) | primary (#6750A4) | hsl(var(--primary)) |
| text | label (#000000) | on-surface (#1C1B1F) | hsl(var(--foreground)) |
| muted | secondaryLabel (#3C3C4399) | on-surface-variant (#49454F) | hsl(var(--muted-foreground)) |
| border | separator (#3C3C434D) | outline (#79747E) | hsl(var(--border)) |
