# Metrics   

|          Metric          |                                  Definition                                  |                         Measurement Method                         |         Target / Threshold         |             Δ (Change Over Time)            |                            Action / Alert                           |
|:------------------------:|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|:----------------------------------:|:-------------------------------------------:|:-------------------------------------------------------------------:|
| Task Success Rate        | % of users completing a task without errors or support tickets               | Correlate API error logs + support ticket tags with doc usage      | ≥ 90%                              | +X% vs last month (goal: upward trend)      | If < 90% OR negative Δ → Review doc flow, add troubleshooting notes |
| Documentation Engagement | % of clicks from search results/navigation into relevant docs                | Analytics on CTR from search and navigation                        | ≥ 25% CTR for top 10 queries       | +X% CTR vs last month (goal: upward trend)  | If < 25% OR negative Δ → Add missing topics, refine metadata        |
| Time to Resolution       | Median time spent on docs before user resumes activity or opens support case | Session analytics (time on page vs. next API call / support case)  | ≤ 5 min on quick start/error pages | –X min vs last month (goal: downward trend) | If > 5 min OR negative Δ → Simplify docs, restructure examples      |
| Documentation Error Rate | % of API errors or tickets traced to doc inaccuracies                        | API logs (invalid params, deprecated calls) + doc mismatch tickets | ≤ 2%                               | –X% vs last month (goal: downward trend)    | If > 2% OR negative Δ → Immediate fix, cross-check with engineering |

## Usage Notes

- Dashboards: Each metric gets a panel (trendline, threshold indicator, red/yellow/green status).
- Ops Rhythm: Review bi-weekly in sprint ops meeting; escalate persistent red metrics to leadership.