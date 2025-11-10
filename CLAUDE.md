# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **Arraial Expo XP** project - a science and technology fair website for Arraial do Cabo municipality. The project is a single-page application (SPA) showcasing the annual science fair, featuring multiple editions, attractions, galleries, and event information.

## Architecture

### Technology Stack
- **Frontend**: Pure HTML5, CSS3, and vanilla JavaScript
- **Styling**: CSS custom properties (variables) with comprehensive design system
- **Images**: Cloudinary CDN for hosted images, placeholder divs for future content
- **Deployment**: Static files ready for web server deployment

### File Structure
```
/
├── index.html              # Main application file (complete SPA)
├── README.md               # Project documentation (Portuguese)
├── nohup.out              # Process output log
└── CLAUDE.md              # This file
```

### Key Features
- **Responsive Design**: Mobile-first approach with breakpoints at 768px
- **Dark/Light Mode**: Automatic system preference detection with manual toggle
- **Interactive Navigation**: Smooth scrolling, mobile hamburger menu
- **Edition Switching**: Dynamic content switching between 2023 and 2025 editions
- **Gallery Filtering**: Interactive filter for photos by year
- **Contact Form**: Functional notification signup with validation
- **Accessibility**: ARIA labels, semantic HTML5 structure

## Design System

### Color Palette (Expo XP Brand)
- **Primary Blue**: `#0288D1` (expo-blue-medium)
- **Dark Blue**: `#01579B` (expo-blue-dark)
- **Light Blue**: `#4FC3F7` (expo-blue-light)
- **Green Medium**: `#26A69A` (expo-green-medium)
- **Light Green**: `#4DB6AC` (expo-green-light)

### CSS Custom Properties
The project uses an extensive design system with CSS custom properties defined in `:root`:
- Spacing: `--space-4` to `--space-32`
- Typography: `--font-size-xs` to `--font-size-4xl`
- Colors: Light/dark mode support with `prefers-color-scheme`
- Shadows: `--shadow-xs` to `--shadow-lg`
- Animations: `--duration-fast`, `--duration-normal`, `--ease-standard`

### Theme System
- **Light Mode**: Default theme with cream backgrounds and dark text
- **Dark Mode**: Activated via `@media (prefers-color-scheme: dark)` query
- **Theme Variables**: All colors automatically adapt based on system preference
- **Smooth Transitions**: Theme changes animate smoothly via CSS transitions

## Development Workflow

### Environment Setup
- **Development Environment**: `https://expoxp.xandy.dev` (staging/review)
- **Production Environment**: `https://expoxp.arraial.rj.gov.br` (after approval)

### Local Development
Since this is a static HTML site, no build process is required:

```bash
# Serve locally (any static server)
python3 -m http.server 8000
# OR
npx serve .
# OR
live-server
```

### Deployment Process
1. **Development**: Deploy to `expoxp.xandy.dev` for review and testing
2. **Approval**: Wait for municipal approval
3. **Production**: Migrate to `expoxp.arraial.rj.gov.br`
4. **Upload**: Transfer files to municipal web server - no build step required

## Content Management

### Updating Edition Information
Edition data is embedded directly in the HTML:
- 2025 edition: `id="edition-2025"` section (lines 1070-1168)
- 2023 edition: `id="edition-2023"` section (lines 1171-1249)

### Gallery Management
Gallery items are in the `#galleryGrid` container (lines 1263-1282):
- Real images use `<img>` tags with Cloudinary URLs
- Placeholder items use `<div class="gallery-item placeholder">`

### Partner Information
Partner data is in the `.partners-grid` section (lines 1300-1341).

## Interactive Features

### JavaScript Functionality
All interactive features are implemented in vanilla JavaScript within `<script>` tags (lines 1425-1549):

1. **Mobile Navigation**: Hamburger menu toggle
2. **Edition Switching**: Tab-based content switching
3. **Gallery Filtering**: Dynamic filter by year
4. **Form Handling**: Notification signup with validation
5. **Scroll Features**: Smooth scrolling, back-to-top button

### Event Listeners
- `navToggle.addEventListener('click')` - Mobile menu
- `editionButtons.forEach()` - Edition switching
- `filterButtons.forEach()` - Gallery filtering
- `notificationForm.addEventListener('submit')` - Form submission
- `window.addEventListener('scroll')` - Back-to-top visibility

## Theme Implementation

### CSS Dark Mode Structure
```css
@media (prefers-color-scheme: dark) {
  :root {
    /* Dark mode color overrides */
    --color-background: var(--color-charcoal-700);
    --color-surface: var(--color-charcoal-800);
    --color-text: var(--color-gray-200);
    /* ... additional dark mode variables */
  }
}
```

### Theme-Aware Components
All components automatically adapt to dark/light mode through CSS custom properties:
- Headers, navigation, and footer backgrounds
- Card surfaces and borders
- Text colors and contrast
- Form inputs and buttons
- Hover and focus states

## Maintenance

### Adding New Editions
1. Duplicate the existing edition section structure
2. Update the `data-edition` attribute and `id`
3. Add corresponding button to `.edition-selector`
4. Update JavaScript to handle new edition

### Image Optimization
- Use Cloudinary for image hosting and optimization
- Maintain aspect ratio with `aspect-ratio: 4/3` for gallery items
- Use placeholder divs for future content

### Theme Customization
- Modify CSS custom properties in `:root` for light mode
- Update dark mode overrides in `@media (prefers-color-scheme: dark)`
- Test theme transitions across all interactive elements

### Performance Considerations
- All CSS is embedded - no external dependencies
- Images are loaded from CDN
- JavaScript is non-blocking and placed at end of body
- CSS custom properties enable consistent theming
- Dark mode uses CSS media queries (no JavaScript required)

## Domain-Specific Context

This is a municipal government website for Arraial do Cabo, RJ, Brazil. The content focuses on:
- Science and technology education
- Environmental sustainability (especially ocean culture)
- Community engagement
- Student achievement showcase

The site serves as both an informational resource and a historical archive for the municipality's educational initiatives.

## Deployment Environments

### Staging (expoxp.xandy.dev)
- Used for development, review, and approval process
- Allows testing and feedback before production deployment
- Can be updated freely during development phase

### Production (expoxp.arraial.rj.gov.br)
- Official municipal domain after approval
- Requires formal deployment process
- Represents the public-facing version for citizens