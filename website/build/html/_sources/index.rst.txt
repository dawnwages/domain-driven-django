.. Domain Driven Django documentation master file, created by
   sphinx-quickstart on Sun Sep  1 15:24:10 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



Welcome
=======

If you’re interested in *Domain-Driven Django*, you’ve likely heard of the versatility of Python and know of the community that Django has created as one of the leading Python web frameworks in the ecosystem. I enjoy that there’s not a culture of romanticizing the patterns in the Django framework; instead we lean on rhetoric about what works and the *separation of concerns* in what can sometimes quickly become complex architecture. 

*Domain-Driven Design*, DDD, is a methodoloy for approaching the creation of software systems where we abstract away the complexities and dive into the patterns that drive the business, listening to the domain experts. Django, the Python web framework for *perfectionists with deadlines*, breaks down the complexity of building a application through dividing it's functionality into smaller, more manageable parts as well as giving its user a common lanuage to describe these patterns. 

This book, *Domain-Driven Django*, is currently being written for the Django entrepreneur, freelancer and angency architect. It will also benefit the product manager, the technical lead, CTO of a Django application. We're highlighting where we can lean into how Django abstracts away intricacies of a modern web system. Although what we're building can vary, abstraction versus implementation will change independently as we approach the problem-space. 

This is an attempt at the application of Django in Domain Driven Design: How do you everage the opinions of the framework to handle technical nuances, and structure business logic for easier refactoring with your domain-experts. Many Django developers, myself included, have spun their wheels attempting to circumvent the opinions of Django. You may have heard the adage "It's just Python" welcoming you into the [arguably] deep waters that is Django. When all else fails you can just do it in Python and build/bring your own (BYO) solution; but you're liable to create a ball of interdependent and cascading effects where weilding Django deftly could otherwise improve the code, its performance and maintainability. We'll cover concepts like *Domain Model versus Django Model*, patterns like CQRS, *Command and Query Responsibility Segregation*, services, communication with domain experts and much more.

Join me on this journey, I'll be sharing some blog posts with comments enabled as I'm writing. **I 
hope to create a dialogue with the Django community that I love so much as I'm writing.**

The timing for this book couldn't be better as I intend to use a few case studies from partner projects with my agency `CMD Limes, LTD <https://cmdlimes.com/>`_. 

.. toctree::
   :maxdepth: 2 

   posts/introduction
   posts/about_the_author


---

.. raw:: html

   <script src="https://giscus.app/client.js"
        data-repo="dawnwages/domain-driven-django"
        data-repo-id="R_kgDOM1gXXA"
        data-category="General"
        data-category-id="DIC_kwDOM1gXXM4CisYw"
        data-mapping="title"
        data-strict="1"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="top"
        data-theme="preferred_color_scheme"
        data-lang="en"
        data-loading="lazy"
        crossorigin="anonymous"
        async>
   </script>
   