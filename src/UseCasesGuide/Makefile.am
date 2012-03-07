#                                               -*- Makefile -*-
#
#  Makefile.am
#
#  (C) Copyright 2005-2012 EDF-EADS-Phimeca
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License.
#
#  This library is distributed in the hope that it will be useful
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
#  @author: $LastChangedBy: schueller $
#  @date:   $LastChangedDate: 2012-02-27 14:48:06 +0100 (lun. 27 févr. 2012) $
#  Id:      $Id: Makefile.am 1539 2012-02-27 13:48:06Z schueller $
#
include $(top_srcdir)/config/common.am

COMMON_SOURCES = \
        $(top_builddir)/src/GenericInformation.tex \
        $(top_srcdir)/src/logoOpenTURNS.jpg \
        docUC_CentralUncertainty_CobWebGraph.tex \
        docUC_CentralUncertainty_CorrelationAnalysis.tex \
        docUC_CentralUncertainty_MomentsEvaluation.tex \
        docUC_CentralUncertainty_QuantileEstimation.tex \
        docUC_CentralUncertainty_SobolIndices.tex \
        docUC_CentralUncertainty_TaylorVarDecomposition.tex \
	docUC_InputBayesian.tex \
        docUC_InputNoData_ComposedDistribution.tex \
        docUC_InputNoData_Copula.tex \
	docUC_InputWithData_CopulaKendallPlotTest.tex \
        docUC_InputNoData_DistManipulation.tex \
        docUC_InputNoData_Mixture.tex \
        docUC_InputNoData_TruncatedDist.tex \
        docUC_InputNoData_UsualDist.tex \
        docUC_InputRandomVector.tex \
        docUC_InputWithData_ChoiceFittedDistributions.tex \
        docUC_InputWithData_CloudDrawing.tex \
        docUC_InputWithData_CopulaEstimation.tex \
        docUC_InputWithData_CSV.tex \
        docUC_InputWithData_EmpiricalDrawing.tex \
        docUC_InputWithData_FittingTests.tex \
        docUC_InputWithData_IndependenceTest.tex \
        docUC_InputWithData_KernelSmoothing.tex \
        docUC_InputWithData_LinearModel.tex \
        docUC_InputWithData_MaxLikelihood.tex \
        docUC_InputWithData_NormalFittingTests.tex \
        docUC_InputWithData_PearsonSpearmanTests.tex \
        docUC_InputWithData_RegressionTest.tex \
        docUC_InputWithData_StatisticalManipulation.tex \
        docUC_InputWithData_TestSameDist.tex \
        docUC_Intro_GeneralCommands.tex \
        docUC_Intro_PythonLib.tex \
        docUC_Intro_PythonStandards.tex \
        docUC_Intro_VerbosityLevel.tex \
        docUC_LoadSave_Load.tex \
        docUC_LoadSave_Save.tex \
        docUC_LowDiscrepancySequences.tex \
        docUC_LSF_Analytical.tex \
        docUC_LSF_DeterministicVar1.tex \
        docUC_LSF_DeterministicVar2.tex \
        docUC_LSF_SomeParticularFunctions.tex \
        docUC_LSF_NMFManipulation.tex \
        docUC_LSF_PythonScript.tex \
        docUC_LSF_Wrapper.tex \
        docUC_MinMax_DetExperimentPlane.tex \
        docUC_MinMax_Evaluation2.tex \
        docUC_MinMax_Evaluation.tex \
        docUC_MinMax_ExpPlaneDrawing.tex \
        docUC_MinMax_MixedDetRandExperimentPlane.tex \
        docUC_MinMax_RandomExperimentPlane.tex \
        docUC_MinMax_SpecifiedExperimentPlane.tex \
        docUC_OVI_FromLSF.tex \
        docUC_OVI_PolyChaosExp.tex \
        docUC_OVI_RandomMixture.tex \
        docUC_OVI_RVExtraction.tex \
        docUC_OVI_SpecializedPolyChaosExp.tex \
        docUC_RandomGenerator.tex \
        docUC_RespSurface_LeastSquaresApprox2.tex \
        docUC_RespSurface_LeastSquaresApprox.tex \
        docUC_RespSurface_PolyChaosDrawings.tex \
        docUC_RespSurface_PolyChaosExpansion.tex \
        docUC_RespSurface_PolyChaosExploitation.tex \
        docUC_RespSurface_TaylorApprox.tex \
        docUC_ThresholdExceedance_DirectionalSampling.tex \
        docUC_ThresholdExceedance_Event.tex \
        docUC_ThresholdExceedance_FORMAlgorithm.tex \
        docUC_ThresholdExceedance_FORMandImportanceSampling.tex \
        docUC_ThresholdExceedance_FORMExploitation.tex \
        docUC_ThresholdExceedance_SimulationAlgoExploitation.tex \
        docUC_ThresholdExceedance_SimulationAlgoParametrisation.tex \
        docUC_ThresholdExceedance_SimulationAlgorithm.tex \
        docUC_ThresholdExceedance_StandardEventManipulation.tex \
        docUC_ThresholdExceedance_StrongMaxTest.tex \
        OpenTURNS_UseCasesGuide.tex \
        useCases_guide_content.tex \
        useCases_guide_title.tex \
        docUC_StocProc_TimeGrid.tex \
        docUC_StocProc_TimeSeries.tex \
        docUC_StocProc_ProcessSample.tex \
        docUC_StocProc_RandomWalk.tex \
        docUC_StocProc_WhiteNoise.tex \
	docUC_StocProc_CompositeProcess.tex \
	docUC_StocProc_DynamicalFunction.tex \
        docUC_StocProc_ARMAIntro.tex \
        docUC_StocProc_ARMA_Creation.tex \
        docUC_StocProc_ARMA_Manipulation.tex \
        docUC_StocProc_NormalIntro.tex \
        docUC_StocProc_TemporalNormalProcess_Creation.tex \
        docUC_StocProc_SpectralNormalProcess_Creation.tex \
	docUC_StocProc_SecondOrderNormalProcess_Creation.tex \
        docUC_StocProc_NormalProcess_Manipulation.tex \
        docUC_StocProc_Process.tex \
        docUC_StocProc_EventProcess.tex \
        docUC_StocProc_MonteCarlo.tex \
        docUC_StocProc_SpectralModel_Estimation.tex \
        docUC_StocProc_BoxCox.tex \
	docUC_StocProc_TrendComputation.tex \
	docUC_StocProc_ARMA_Estimation_Whittle.tex \
	docUC_StocProc_SpectralModel_Creation.tex 

COMMON_SOURCES += \
	arma1D_prediction.png \
	arma1D_predictions.png \
	arma1D_realization.png \
	arma1D_realizations.png \
        AxialGrid.png \
        beta_1.png \
        beta_2.png \
        beta_QQplot.png \
        BoxGrid.png \
        cdf_Bernoulli.png \
        cdf_Binomial.png \
        cdf_Geometric.png \
        cdf_Histogram.png \
        cdf_Mixture.png \
        cdf_Poisson.png \
        cdf_UserDefined.png \
        cdf_ZipfMandelbrot_1.png \
        ClaytonCopula.png \
        cloud1.png \
        cloud2.png \
        cobWeb.png \
        ComposedDistribution_isoPDF_12.png \
        ComposedDistribution_isoPDF_13.png \
        ComposedDistribution_isoPDF_23.png \
        CompositeGrid.png \
        contour2D_2.png \
        contour2D_tulipe.png \
        copula_estimation.png \
        EventProbabilityIndexMarginalSensitivityDrawing.png \
        FactorialGrid.png \
        FrankCopula.png \
        GumbelCopula.png \
        HasoferReliabilityIndexMarginalSensitivityDrawing.png \
        HenryLineTestFalse.png \
        HenryLineTestRight.png \
	hist_Data.png \
        ImportanceFactorsDrawingFORM.png \
        ImportanceFactorsDrawingQuadraticCumul.png \
        IndependentCopula.png \
        initSample.png \
	KendallPlotCopulaBad.png \
	KendallPlotCopula.png \
	KendallPlotSample.png \
	KendallPlotSampleBad.png \
        kernelSmoothing_boundary_cdf.png \
        kernelSmoothing_boundary_pdf.png \
        kernelSmoothingBWSel_cdf.png \
        kernelSmoothingBWSel_pdf.png \
        kernelSmoothing_cdf.png \
        kernelSmoothing_pdf.png \
        linearRegression_Graph.png \
        linearRegression_GraphWrong2.png \
        linearRegression_GraphWrong.png \
        linearRegression_residualGraph.png \
        linearRegression_residualGraphWrong2.png \
        linearRegression_residualGraphWrong.png \
	MonteCarloEventProcessConvergency.png \
        NormalCopula.png \
	PCE_CharlierPolynomials.png \
        PCE_comparisonModels.png \
        PCE_JacobiPolynomials_VariableE.png \
        PCE_JacobiPolynomials_VariableI.png \
	PCE_KrawtchoukPolynomials.png \
        PCE_LaguerrePolynomials_VariableF.png \
        PCE_LegendrePolynomials_VariableL.png \
        pdf_Arcsine.png \
        pdf_Bernoulli.png \
        pdf_Beta_1.png \
        pdf_Beta_2.png \
        pdf_Beta_3.png \
	pdf_Beta_4.png \
        pdf_Beta_5.png \
        pdf_Beta_6.png \
        pdf_Beta_7.png \
        pdf_Binomial.png \
        pdf_Burr_1.png \
        pdf_Burr_2.png \
        pdf_Burr_3.png \
        pdf_Chi_1.png \
        pdf_ChiSquare_1.png \
        pdf_ChiSquare_2.png \
        pdf_ChiSquare_3.png \
        pdf_Epanechnikov.png \
        pdf_Exponential.png \
        pdf_FisherSnedecor_1.png \
        pdf_FisherSnedecor_2.png \
        pdf_Gamma_1.png \
        pdf_Gamma_2.png \
        pdf_Gamma_3.png \
        pdf_Geometric.png \
        pdf_Gumbel.png \
        pdf_Histogram.png \
        pdf_InverseNormal_1.png \
        pdf_InverseNormal_2.png \
        pdf_Laplace.png \
        pdf_Logistic.png \
        pdf_LogNormal.png \
        pdf_LogUniform.png \
        pdf_Mixture.png \
        pdf_NonCentralChiSquare_1.png \
        pdf_NonCentralChiSquare_2.png \
        pdf_NonCentralStudent.png \
        pdf_Normal.png \
        pdf_Poisson.png \
        pdf_Rayleigh.png \
        pdf_Rice_1.png \
        pdf_Rice_2.png \
        pdf_Student.png \
        pdf_Trapezoidal.png \
        pdf_Triangular.png \
        pdf_TruncatedNormal_1.png \
        pdf_TruncatedNormal_2.png \
        pdf_TruncatedNormal_3.png \
        pdf_TruncatedNormal_4.png \
        pdf_Uniform.png \
        pdf_UserDefined.png \
        pdf_Weibull_1.png \
        pdf_Weibull_2.png \
        pdf_ZipfMandelbrot_1.png \
        RandomMixture_cdf.png \
        RandomMixture_pdf.png \
	randomwalk1D_continuous.png\
	randomwalk1D_discrete.png \
	randomwalk2D_continuous.png \
	randomwalk2D_discrete.png \
        ranksSample.png \
        ScaledAxialGrid.png \
        ScaledBoxGrid.png \
        ScaledCompositeGrid.png \
        ScaledFactorialGrid.png \
	spectralNormal2D_realization.png \
	spectralNormal2D_realizations.png \
        StrongMaxTest_vicinity.png \
	temporalNormal2D_realization.png \
	temporalNormal2D_realizations.png \
        TranslatedScaledAxialGrid.png \
        TranslatedScaledBoxGrid.png \
        TranslatedScaledCompositeGrid.png \
	TranslatedScaledFactorialGrid.png \
	truncatedDistribution_cdf.png \
	truncatedDistribution_pdf.png \
        weibull_QQplot.png \
        whitenoise_realization.png \
        whitenoise_realizations.png \
	script_bayesianRandomVector.py \
        script_cloud1.py \
        script_cloud2.py \
        script_CobWeb.py \
        script_composedDistribution.py \
        script_CopulaEstimation.py \
        script_copula.py \
        script_DataHist.py \
        script_distribution_manipulation.py \
	script_ExperimentPlanes.py \
	script_FORM.py \
        script_HenryLine.py \
        script_Histogram.py \
	script_KendallPLot.py\
        script_kernelMixture.py \
        script_kernelSmoothing2.py \
        script_kernelSmoothing.py \
        script_linearRegression.py \
        script_MaximumLikelihoodEstimation.py \
        script_mixture.py \
	script_PolynomialChaosExpansion.py \
	script_QQPlot.py \
	script_quadraticCumul.py \
	script_RandomMixture.py \
	script_RandomWalk.py \
        script_truncatedDistribution.py \
        script_usualDistribution.py \
	welchValidation.png \
	script_WhiteNoise.py \
	script_Welch.py \
        script_ARMA.py \
        script_NormalProcess.py \
        script_MonteCarloProcess.py \
	script_estimate_arma_whittle.py

PDF_SOURCES = \
        Math_Notations.sty \
        OpenTURNS_UseCasesGuide.sty \
        FigureStrongMaxTest.pdf \
        halton_cloud.pdf \
        mersenne_twister_cloud.pdf \
	pdf_bayesianRandomVector.pdf\
        poutre.pdf \
	randomwalk1D_continuous.pdf \
	randomwalk1D_discrete.pdf \
	randomwalk2D_continuous.pdf \
	randomwalk2D_discrete.pdf \
        reverseHalton_cloud.pdf \
        sobol_cloud.pdf 

XML_SOURCES = \
        Math_Notations.plt \
        OpenTURNS_UseCasesGuide.plt \
        FigureStrongMaxTest.png \
	halton_cloud.png \
        mersenne_twister_cloud.png \
	pdf_bayesianRandomVector.png\
        poutre.png \
	reverseHalton_cloud.png \
        sobol_cloud.png

OpenTURNS_UseCasesGuide.pdf: $(COMMON_SOURCES) $(PDF_SOURCES)

OpenTURNS_UseCasesGuide.xml: $(COMMON_SOURCES) $(XML_SOURCES)

pdf-local: OpenTURNS_UseCasesGuide.pdf

doc_DATA  = OpenTURNS_UseCasesGuide.pdf
EXTRA_DIST = $(COMMON_SOURCES) $(PDF_SOURCES)

if WITH_TRALICS
if WITH_LIBXSLT
html-local: OpenTURNS_UseCasesGuide.tgz
install-html-local: OpenTURNS_UseCasesGuide.installed
EXTRA_DIST += $(XML_SOURCES)
endif
endif
