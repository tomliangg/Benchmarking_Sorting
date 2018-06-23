# Benchmarking_Sorting-CMPT353_e6_p2
<h3>This repo is created for documentation purpose. The repo contains my personal work toward the SFU CMPT353 (Computational Data Science) course. You may use my solution as a reference. The .zip archive contains the original exercise files. For practice purpose, you can download the .zip archive and start working from there.</h3>

<p><a href="https://coursys.sfu.ca/2018su-cmpt-353-d1/pages/AcademicHonesty">Academic Honesty</a>: it's important, as always.</p>
<br/>
<p> The task of this exercise is to use statistical tests (namely ANOVA and post hoc analysis) to benchmark 7 different sorting algorithms. The 7 sorting algorithms are alreay pre-implemented. You job is to firstly write a program to create/generate time data which will be stored into a .csv file. Afterwards, implement a data analysis program which takes in the data .csv file and perform the stat tests there.</p>
<p><b>Note:</b> I don't have permission to run my script on the SFU cloud gateway so I didn't try to meet the restriction #1. Nevertheless, the code takes around 35 seconds to run on my old Surface Pro 3 (4GB RAM).</p>
<br/>
<p>Below is the exercise description </p>
<hr>

<h2 id="h-benchmarking-sorting">Benchmarking Sorting</h2>
<p>For this question, you will be benchmarking some code to see how it performs, and analysing the results for statistical significance. Throughout this course, we have been doing what most people do: run the program a few times (maybe with <code>%timeit</code>) and looking at the averages. We now know that isn't quite enough to draw conclusions.</p>
<p>In the provided <code>implementations.py</code>, I have implemented several sorting algorithms in different ways. Each sorts NumPy arrays not-in-place (i.e. they do not modify their input array, but return a new array).</p>
<p>The question is simple: what can you say about which implementations are faster/slower?</p>
<h3 id="h-data-creation">Data Creation</h3>
<p>We are concerned with the seven sorting implementations given in the <code>all_implementations</code> array: <code>qs1</code>, <code>qs2</code>, <code>qs3</code>, <code>qs4</code>, <code>qs5</code>, <code>merge1</code>, <code>partition_sort</code>. As you might guess, there are several <a href="https://en.wikipedia.org/wiki/Quicksort">QuickSort</a> implementations, one <a href="https://en.wikipedia.org/wiki/Merge_sort">Merge Sort</a>, and one QuickSort-like thing I have named <span>&ldquo;</span>partition sort<span>&rdquo;</span>.</p>
<p>Write a program <code>create_data.py</code> that generates random arrays, and uses <a href="https://docs.python.org/3/library/time.html">time.time</a> to measure the <a href="https://en.wikipedia.org/wiki/Wall-clock_time">wall-clock time</a> each function takes to sort them. You <strong>may</strong> write loops in the <code>create_data.py</code> program.</p>
<p>We are concerned about (1) arrays with random integers, which are randomly sorted, (2) arrays that are as large as possible, and (3) being able to meaningfully analyse the results.  [Note: see the restrictions below.]</p>
<p>You're going to want enough data points that you can assume normality for your analysis. It's likely that your results will be somewhat-normally-distributed, but not precisely. You'll need a large enough \(n\) to proceed with tests that assume normality anyway.</p>
<p>You can import <code>implementations.py</code> and iterate through the relevant sorting functions like this:</p>
<pre class="highlight lang-python">import time
from implementations import all_implementations
# ...
for sort in all_implementations:
    st = time.time()
    res = sort(random_array)
    en = time.time()</pre>
<p>In this program, create a DataFrame in a format that makes sense, and save it as <code>data.csv</code>, something like this:</p>
<pre class="highlight lang-python">data.to_csv('data.csv', index=False)</pre>
<h3 id="h-restriction-1-processor-time">Restriction #1: processor time</h3>
<p>Your <code>create_data.py</code> must <strong>run in at most 60 seconds on <code>gateway.sfucloud.ca</code></strong> (single-threaded). You should be able to SSH to this server (<code>ssh USERID@gateway.sfucloud.ca</code>) and run your code there; the modules you need should be installed.</p>
<p>You can check the running time, or enforce a time limit (respectively) with commands like these:</p>
<pre class="highlight lang-bash">time python3 create_data.py # just check the time
timeout -s SIGKILL 60 python3 create_data.py # kill after 60 seconds</pre>
<p>This restriction is imposed to limit the number of samples you can collect. This is generally realistic: I have sized this question so you don't have to wait too long to get data, but often the code you're benchmarking will take so long that it's prohibitive to collect thousands of data points. My intention is to give you a realistic data-collection limit, without making you wait overnight for results.</p>
<p>Forcing you to use <code>gateway.sfucloud.ca</code> will also cause a certain amount of noise in your samples due to <a href="https://en.wikipedia.org/wiki/Cloud_computing_issues#Performance_interference_and_noisy_neighbors">noisy neighbours</a>. This is also a realistic problem to have.</p>
<h3 id="h-restriction-2-run-count">Restriction #2: run count</h3>
<p>When creating your data, you must <strong>run each sorting implementation an equal number of times</strong>.</p>
<p>In this artificial situation, you could run the test a few times, decide which sorting functions are more or less critical to have data for, and bias your experiment to collect more of the nearly-equal values. That's not realistic in general, where it might not be feasible to run the experiment a dozen times. (Technically, something like this could be done as a <a href="https://en.wikipedia.org/wiki/Pilot_experiment">pilot study</a>, but I'm going to call it <span>&ldquo;</span>cheating by knowing the answer before your experiment<span>&rdquo;</span>.)</p>
<h3 id="h-data-analysis">Data Analysis</h3>
<p>Once you have some data, you'll need to do some analysis to decide which sorting implementations are faster/slower/indistinguishable. You will need a statistical test that can be used to determine if the means of multiple samples are different, and then decide which ones. Hmm<span>&hellip;</span></p>
<p>In your analysis, you can almost certainly apply the lesson from the <span>&ldquo;</span>It's Probably Okay<span>&rdquo;</span> section in lecture: if you have more than about 40 data points and they are reasonably-normal-looking, then you can use a parametric test.</p>
<p>Create a program <code>analyse_data.py</code> that reads the <code>data.csv</code> that you produced above and does the relevant statistical analysis. It should <code>print</code> the information you used to answer question 3 below, but there is no specific format required.</p>
<h2 id="h-questions">Questions</h2>
<p>Answer these questions in a file <code>answers.txt</code>.</p>
<ol><li>In the A/B test analysis, do you feel like we're p-hacking? How comfortable are you coming to a conclusion at \(p&lt;0.05\)?
</li><li>If we had done T-tests between each pair of sorting implementation results, how many tests would we run? If we looked for \(p&lt;0.05\) in them, what would the probability be of having all conclusions correct, just by chance? That's the effective p-value of the many-T-tests analysis. [We could have done a <a href="https://en.wikipedia.org/wiki/Bonferroni_correction">Bonferroni correction</a> when doing multiple T-tests, which is a fancy way of saying <span>&ldquo;</span>for \(m\) tests, look for significance at \(\alpha/m\)<span>&rdquo;</span>.]
</li><li><strong>Give a ranking</strong> of the sorting implementations by speed, including which ones could not be distinguished. (i.e. which pairs could our experiment not conclude had different running times?)
</li></ol>
