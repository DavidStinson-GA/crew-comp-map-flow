voice = """
<h1>
  <span class="headline">Modularization Documentation</span>
  <span class="subhead">Style Guide - Technical Voice</span>
</h1>

This guide outlines standards for technical writing during the modularization work at GA. It will help you achieve a consistent technical voice. Adhering to these guidelines for all technical modular content ensures a unified content presentation and a seamless transition between lectures for learners.

## Get cozy

Write conversationally. If a sentence sounds formal or distant when read aloud, consider revising it. Aim for a friendly, personable tone. Use contractions. Avoid using Latin abbreviations like e.g., or i.e.

## But not too cozy

Remember, someone else might present your written content. Allow instructors to infuse their style, but avoid jokes that may not resonate with all. Steer clear of idioms, scare quotes, and overly colloquial phrases. They might be misunderstood by native English speakers and can be especially confusing for ESL learners.

## Write inclusively

For guidelines on inclusive writing, refer to the **Inclusivity & Best Practices Guide** in the [General Assembly Brand Guide](https://drive.google.com/file/d/1eldhzkHPyS7T2_NCryMm-IFY1gKsxNYY/view) for general guides on writing inclusively. When writing code, also consult the [Technical Style Guide](./technical-style.md).

## We're in it together

Engage the reader as a fellow traveler. Use inclusive language like **let's, we, and us**.

Be empathetic. Foresee the reader's challenges and address them. Never omit steps. If a visual might explain a concept better, discuss this with your team.

Celebrate achievements! 🎉

## Get to the point

Prioritize essential information. Structure your writing for easy scanning to aid live lectures. Present crucial details prominently, not buried in larger paragraphs. Keep it simple.

Be concise. Eliminate redundant words or sentences. Avoid unnecessary adverbs, particularly those that are subjective, like "quickly" or "easily."

## Precise but brief

Avoid over-explaining a concept. Get the point across, but don't repeat it.

When possible, use words that have one clear meaning. Words that can act as both nouns and verbs can be easily misunderstood and should be used carefully.

Use one term consistently to represent a concept. Sounding repetitive is preferable to introducing confusion by switching between multiple terms for the same thing.

Start new paragraphs more often than you would in formal writing.

## Impress to connect, connect to impress

Strive to deliver accurate and digestible content. While occasional mistakes are inevitable, unnoticed errors in the curriculum quickly erode trust from both students and instructors. Accurate, smoothly delivered content fosters better connections and makes it easier for instructors to do their jobs.

Don't make potentially controversial changes to the curriculum without bringing a group of other voices into the room.

## Express intent

Our written content should stand alone and be comprehensible without the aid of a video or live presentation. Don't rely on another instructor to read into your writing cues and know to expand on an idea.

If a topic is important enough that the content is incomplete without it, always opt to include it.

## Examine your assumptions

Assume that learners are intelligent and capable of learning, but be careful making any further assumptions. Don't assume they are familiar with technical or business jargon - when using these terms, you should define them.
"""

writing_learning_objectives = """
# Writing Learning Objectives

Bloom's Taxonomy is a widely adopted instructional design model that scaffolds learning objectives from "low level learning" objectives (knowledge, comprehension) through to "high level learning" objectives (evaluation, synthesis).

It is important to remember that we work with busy, professional, adult learners, often high achievers. We aim to teach through stories and through action, and should avoid entire lectures that are completely lower level whenever possible.

Remember, our learners' end goals is almost always being able to use this information in their jobs.

Do not use Bloom's verbs that are not measurable.

## Good Learning Objectives

At General Assembly, we define a good learning objective as:

SIMPLE. Clearly and plainly phrased. Don't make me think! Not yet! 
CLEAR. Someone who hasn't taken the lesson yet can understand it. 
VALUABLE. A user or client would "pay" for it (with time and/or money). 
REALISTIC. Reflects an action that someone is likely to take in real life. 
MEASURABLE. Can be evaluated. 

To further expand on the above, here are some examples of weak learning objectives, and how they can be improved and made stronger:

| Objectives are ... | Weak example | Strong example | How it was improved |
| ------------------ | ------------ | -------------- | ------------------- |
| SIMPLE. Plainly Phrased: (Avoid Double Barrelled LOs) | Choose graphics and illustrations that best illuminate various types of data. | Choose the most appropriate graphics to communicate your data story. | Refine language to be more direct and clear. |
| CLEAR. Written for the "before" user, who presumably does not yet know the topic. | Identify the stages of the customer decision journey. | Describe six distinct phases a person goes through when making a purchase, known as the "customer decision journey". | Put yourself in the shoes of someone who has no familiarity with the subject and what they might think it means. |
| VALUABLE. Worth a learner / client's time and $$$. | Describe how beacon technology works. | Identify opportunities to use beacons to drive consumer engagement and sales. | 1. Start with a real problem the audience has. 2. If you don't know what this is as related to this lesson, get clarity from the EPM. 3. If the answer is 1-2 googles away, it's probably not worth a buyer's $$$. Dig deeper. |
| REALISTIC. Reflects the actions learners need to take in real life. | Examine how data visualizations can help validate data sets and help explore relationships. | Use data visualizations to validate and explore your data. | Practice the "five whys" - why would anyone need to know this? Keep asking why until you get to what knowing it will actually enable them to do. |
| MEASURABLE. Can be evaluated. | Give viewability to the appropriate emphasis in your strategy and measurement. | Identify campaign conditions in which viewability is a critical metric. | Consider: Can you visualize a knowledge check or assessment question that effectively tests this?  If for in person classes, can you imagine an exercise or project? Then ask yourself, is that assessment question or project useful? |

## Goals vs. Learning Objectives

It's important to understand the difference between a goal and a learning objective.

## Goals

Why someone purchases a learning program - what they are hoping to achieve.

Met through the fulfillment of learning objectives AND action by the learner. 

In a corporate context, typically requires change management led by leadership.

May require organizational design, technology purchases, etc. to achieve.

In a campus context, the most common end goal is a career change or advancement.

Goals should be defined by CPMs. (Commercial Product Managers)

## Learning Objectives

This learning, in combination with learner action, enables people to achieve their goals.

These are defined/summarized at each level of the program - a unit, a module, etc.

Owned and drafted by the Learning team, in conjunction/partnership with SMEs.

GA is responsible for learners achieving these through the design and instruction of the course - these are our commitments to the learner.

Learners/clients may meet LOs but still dislike the learning experience or fail to meet their goals if they either had unclear goals, chose/were guided toward the wrong program for their goals, or did not take the actions required to use the learning to fulfill their goals.
"""

documentation = {
  "voice": voice,
  "writing_learning_objectives": writing_learning_objectives
}