# shadcn/ui Official Rules (from shadcn-ui/ui `skills/shadcn`)

Distilled from github.com/shadcn-ui/ui (MIT © shadcn). Apply whenever output is React + shadcn/ui. For the shadcnuikit visual language see `shadcn-dashboard-patterns.md`.

## Principles
1. Use existing components first (`npx shadcn@latest search`, community registries) before custom UI.
2. Compose, don't reinvent: Settings = Tabs + Card + form controls. Dashboard = Sidebar + Card + Chart + Table.
3. Built-in variants before custom styles (`variant="outline"`, `size="sm"`).
4. Semantic colors only (`bg-primary`, `text-muted-foreground`), never `bg-blue-500`.

## Styling
- `className` for layout, not for overriding component color/typography.
- No `space-x/y-*`; use `flex` + `gap-*` (`flex flex-col gap-4`).
- `size-10` not `w-10 h-10`. `truncate` not the 3-class combo.
- No manual `dark:` color overrides; tokens handle it. `cn()` for conditional classes.
- No manual `z-index` on Dialog/Sheet/Popover.

## Forms
- `FieldGroup` + `Field` + `FieldLabel` + `FieldDescription`; never div + space-y.
- Validation: `data-invalid` on `Field`, `aria-invalid` on the control; disabled: `data-disabled` on Field + `disabled` on control.
- `InputGroup` + `InputGroupInput`/`InputGroupAddon` for icons/buttons inside inputs.
- 2–7 options → `ToggleGroup`, not looped Buttons. Related checkboxes/radios → `FieldSet` + `FieldLegend`.

## Composition
- Items inside their Group (`SelectItem` in `SelectGroup`, `DropdownMenuItem` in `DropdownMenuGroup`, `CommandItem` in `CommandGroup`).
- Custom triggers via `asChild` (Radix) or `render` (Base UI).
- Dialog/Sheet/Drawer always have a Title (`sr-only` if hidden).
- Full Card anatomy: `CardHeader / CardTitle / CardDescription / CardContent / CardFooter` (+ `CardAction`).
- Button has no `isLoading`: compose `Spinner` + `data-icon` + `disabled`.
- `TabsTrigger` inside `TabsList`. `Avatar` always has `AvatarFallback`.
- Use `Alert` for callouts, `Empty` for empty states, `Separator` not `<hr>`, `Skeleton` not custom pulse divs, `Badge` not styled spans. Toast: `sonner` (Radix) or `toast` (Base UI).
- Chat: `MessageScroller` + `Message` + `Bubble`; `Attachment`; `Marker` for system notes.

## Icons
- In buttons: `data-icon="inline-start" | "inline-end"`; no size classes on icons inside components; pass icon components, not string keys.

## Component selection
| Need | Use |
|---|---|
| Action | `Button` variant |
| Inputs | `Input`, `Select`, `Combobox`, `Switch`, `Checkbox`, `RadioGroup`, `Textarea`, `InputOTP`, `Slider` |
| 2–5 option toggle | `ToggleGroup` |
| Data | `Table`, `Card`, `Badge`, `Avatar` |
| Navigation | `Sidebar`, `NavigationMenu`, `Breadcrumb`, `Tabs`, `Pagination` |
| Overlays | `Dialog`, `Sheet` (side), `Drawer` (bottom), `AlertDialog` (confirm) |
| Feedback | toast/sonner, `Alert`, `Progress`, `Skeleton`, `Spinner` |

## Key patterns
```tsx
<FieldGroup><Field><FieldLabel htmlFor="email">Email</FieldLabel><Input id="email" /></Field></FieldGroup>
<Field data-invalid><FieldLabel>Email</FieldLabel><Input aria-invalid /><FieldDescription>Invalid email.</FieldDescription></Field>
<Button><SearchIcon data-icon="inline-start" />Search</Button>
<Badge variant="secondary">+20.1%</Badge>   // not <span className="text-emerald-600">
```
CLI: never hand-decode preset codes; use `npx shadcn@latest preset decode|apply`, `init --preset`.
