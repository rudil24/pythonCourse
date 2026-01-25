# Product Requirements Document (PRD): [Feature Name]

| Metadata | Details |
| :--- | :--- |
| **Status** | `Draft` / `In Review` / `Approved` / `In Development` |
| **Owner** | @[YourName] |
| **Team** | [e.g., Core Product, Growth] |
| **Target Date** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |
| **Epic/Ticket** | [Link to Jira/Linear Ticket] |

> **Instructions for Junior PMs:**
> * Keep sections concise. Use bullet points over paragraphs.
> * If a section is not relevant, mark it N/A; do not delete it (AI parsers prefer consistent structure).
> * **Crucial:** The "Technical Context" section is the most important part for our AI coding assistants.

---

## 1. Context & Problem Statement
* **The "Why":** [One sentence explaining why we are building this. What user pain point are we solving?]
* **Current State:** [Briefly describe how users handle this today / the existing workaround.]
* **Desired State:** [Briefly describe the world after this feature exists.]

## 2. User Stories & Acceptance Criteria
*Format: As a [user type], I want to [action], so that [benefit].*

### Story 1: [Short Title]
* **User Story:** As a...
* **Acceptance Criteria (Gherkin Syntax preferred for AI):**
    * `GIVEN` [context, e.g., user is logged in]
    * `WHEN` [action, e.g., user clicks "Submit"]
    * `THEN` [result, e.g., the modal closes and a toast appears]
* **Priority:** P0 (Blocker)

### Story 2: [Short Title]
* **User Story:** ...
* **Acceptance Criteria:** ...
* **Priority:** P1 (High)

---

## 3. Technical Specifications (AI Context)
> **Note to PM:** This section bridges the gap between product and engineering. Fill this out with your Tech Lead.

### 3.1 Data Model Changes
*Does this require schema changes? Define them here.*
```json
// Example JSON representation of new fields
{
  "table": "users",
  "fields_to_add": {
    "is_beta_tester": "boolean (default: false)",
    "last_login_metadata": "jsonb"
  }
}
```

### 3.2 API Logic / Pseudocode
*Describe the logic flow step-by-step. AI agents rely on this to write business logic functions.*
1.  **Endpoint:** `POST /api/v1/resource`
2.  **Validation:** Check if user has `premium` role. If not, return 403.
3.  **Process:**
    * Fetch current data from DB.
    * Calculate X using `UtilityFunctionY`.
    * Update record.
4.  **Response:** Return 200 OK with `{ id: "123", status: "success" }`.

### 3.3 Dependencies & Constraints
* **Tech Stack:** [e.g., React, Node.js, PostgreSQL]
* **Existing Components to Reuse:** [e.g., `<Button />`, `<Modal />` from Design System]
* **Performance:** [e.g., Response must be under 200ms]

---

## 4. UI/UX Design
* **Figma Link:** [Insert Link]
* **Key UI States:**
    * [ ] **Empty State:** What happens when there is no data?
    * [ ] **Loading State:** Skeleton loader or spinner?
    * [ ] **Error State:** What does the user see if the API fails?
* **Copy/Text:** [Link to Copy Doc or list key phrases here]

---

## 5. Analytics & Observability
*What do we need to track to know if this is successful?*

| Event Name | Trigger | Properties to Capture |
| :--- | :--- | :--- |
| `feature_clicked` | User clicks the main CTA | `user_id`, `page_location` |
| `process_completed` | User finishes the flow | `time_taken`, `success_status` |

---

## 6. Open Questions / Risks
* [ ] Question 1: [e.g., Do we need legal approval for this text?]
    * *Resolution:* [Answer]
* [ ] Risk 1: [e.g., This might impact legacy users on version 1.0]
    * *Mitigation:* [Plan]

---

## 7. Rollout Plan
* [ ] **Phase 1:** Internal Testing (Dev/Staging)
* [ ] **Phase 2:** Beta Group (10% of users) - *Date: YYYY-MM-DD*
* [ ] **Phase 3:** General Availability (100%)